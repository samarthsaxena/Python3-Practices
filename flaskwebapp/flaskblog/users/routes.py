from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import db, bcrypt
from flaskblog.models import User, Post
from flaskblog.users.forms import (RegistrationForm, LoginForm,
                                   UpdateAccountForm, RequestResetForm,
                                   ResetPasswordForm)
from flaskblog.users.utils import save_picture, send_reset_email


users = Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    # If a user is already logged in, then route to home
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    # Access this registration form through an object of this class
    form = RegistrationForm()

    # When the form is submitted the current configs don't check very much the details about data fieldset
    # Here we shall include validated_on_submit() in order to avoid such issue
    if form.validate_on_submit():
        # store hashed password as UTF-8 String instead of bytes
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
        # Create this user with hashed password
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created {form.username.data}, Enjoy the services !', 'success')
        return redirect(url_for('users.login'))

    # And pass thi regitration form object to render_template() to include it's webelements
    return render_template('register.html', title='Register Here', form=form)


# Almost the same thing goes here (Same as register())
@users.route("/login", methods=['GET', 'POST'])
def login():
    # If a user is already logged in, then route to home
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            # In case or redirection, App needs to know what was that page user was trying to access
            next_page = request.args.get('next')  # args is a dictionary but no ['next'] is used to avoid exceptions
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash(f'Login failed! Please check email and password.', 'danger')
    return render_template('login.html', title='Login Form', form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route("/account", methods=['GET', 'POST'])
@login_required  # to make this view available iff user is authenticated already.
# To make application aware of this default functionality, we'd add login_view in login_manager.
def account():
    form = UpdateAccountForm()

    if form.validate_on_submit():
        # to save the changes in Profile picture
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash(f'Your account has been updated !', category='success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account Info', image_file=image_file, form=form)



@users.route('/user/<string:username>')
def username_post(username):
    # posts = Post.query.all()
    page = request.args.get('page', 1, type=int)
    # to filter the posts based on username that posted it
    user = User.query.filter_by(username=username).first_or_404()
    # To show the most recent post at the beginning for this user
    posts = Post.query \
        .filter_by(author=user) \
        .order_by(Post.date_posted.desc()) \
        .paginate(per_page=PER_PAGE_POSTS)
    return render_template('user_post.html', posts=posts, user=user)



@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RequestResetForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash(f'Password reset instructions have been sent to {user.email}', 'alert alert-success')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    user = User.verify_reset_token(token)
    # In case token is expired or an invalid string of chars
    if user is None:
        flash(f'Invalid request ! reason: Invalid token', 'warning')
        return redirect(url_for('users.reset_request'))

    form = ResetPasswordForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
        # New hashed password
        user.password = hashed_password
        db.session.commit()
        flash(f'Your password has been update {user.email}', 'success')
        return redirect(url_for('users.login'))

    return render_template('reset_token.html', title='Reset Password', form=form, user=user)
