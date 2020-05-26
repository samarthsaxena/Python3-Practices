import os
import secrets

from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog import app, db, bcrypt, mail
from flaskblog.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                             PostForm, RequestResetForm, ResetPasswordForm)
from flaskblog.models import User, Post
from flask_mail import Message

"""posts = [
    {
        "author": 'Samarth Saxena',
        'title': 'Blog Post 1',
        'content': 'First Post content.',
        'date_posted': '11/05/2019'
    },
    {
        'author': 'Alex Parish',
        'title': 'Blog Post 2',
        'content': 'Second Post content.',
        'date_posted': '12/05/2019'
    },
    {
        'author': 'Steve Rogers',
        'title': 'Blog Post from Captain America',
        'content': 'Third Post content.',
        'date_posted': '13/05/2019'
    },
    {
        'author': 'Bruce Wayne',
        'title': 'Blog Post etc tec',
        'content': 'fourth Post content.',
        'date_posted': '12/05/2019'
    }

]
"""

PER_PAGE_POSTS: int = 5


@app.route('/test')
def hello():
    return render_template('testpage.html')


@app.route("/")
@app.route('/home')
def home():
    # posts = Post.query.all()
    page = request.args.get('page', 1, type=int)
    # To show the most recent post at the beginning,
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=PER_PAGE_POSTS)
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


# in this route methods kwargs helps to accept GET and POST methods
# hence avoiding below error
# ERROR:
# "Method Not Allowed
# The method is not allowed for the requested URL."
@app.route("/register", methods=['GET', 'POST'])
def register():
    # If a user is already logged in, then route to home
    if current_user.is_authenticated:
        return redirect(url_for('home'))

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
        return redirect(url_for('login'))

    # And pass thi regitration form object to render_template() to include it's webelements
    return render_template('register.html', title='Register Here', form=form)


# Almost the same thing goes here (Same as register())
@app.route("/login", methods=['GET', 'POST'])
def login():
    # If a user is already logged in, then route to home
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            # In case or redirection, App needs to know what was that page user was trying to access
            next_page = request.args.get('next')  # args is a dictionary but no ['next'] is used to avoid exceptions
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'Login failed! Please check email and password.', 'danger')
    return render_template('login.html', title='Login Form', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    # Ignore the name of original file, save the extension
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    # resize the picture before saving
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    # Save the compressed picture in profile_pics dir with random name
    i.save(picture_path)

    # Now return the name of the picture file from here
    # (i.e. to answer : what is the name of this user's profile picture)
    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
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
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account Info', image_file=image_file, form=form)


@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        flash(f'Post \'{form.title.data}\' has been created! ', 'success')
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post !', form=form, legend='New Post')


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    # Only the user who created the post can update the post
    if post.author != current_user:
        # if the current user is not an owner of this post, abort the action
        abort(403)
    # Otherwise current user can update the post
    form = PostForm()

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()

        flash(f'Your post \'{post.title}\' has been updated', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        # Auto populate the title and content w.r.t. existing post's data
        form.title.data = post.title
        form.content.data = post.content

    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


# Route will just work with form post request. IMP!
@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()

    flash(f'Your post {post.title} has been deleted', 'success')
    return redirect(url_for('home'))


@app.route('/user/<string:username>')
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


# for sending email
def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@app.com',
                  recipients=[user.email])
    msg.body = f'''To Reset your password, Please visit the below link.

{url_for('reset_token', token=token, _external=True)}

<b> If you DID NOT make this request. Please ignore this mail! </b>
'''
    # send the mail
    mail.send(msg)


@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RequestResetForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash(f'Password reset instructions have been sent to {user.email}', 'alert alert-success')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    user = User.verify_reset_token(token)
    # In case token is expired or an invalid string of chars
    if user is None:
        flash(f'Invalid request ! reason: Invalid token', 'warning')
        return redirect(url_for('reset_request'))

    form = ResetPasswordForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
        # New hashed password
        user.password = hashed_password
        db.session.commit()
        flash(f'Your password has been update {user.email}', 'success')
        return redirect(url_for('login'))

    return render_template('reset_token.html', title='Reset Password', form=form, user=user)
