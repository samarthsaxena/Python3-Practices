#!/usr/bin/env3 python3

from flask import Flask, render_template, url_for, flash, redirect

# import the Registration and login forms from forms module you just created
from forms import RegistrationForm, LoginForm

# Initialize this App to FlaskApp
app = Flask(__name__)

# Add a secret key to Application, in order to protect against Xss and hacks
# Generated from python3 secrets module with token_hex(soem int value)
app.config['SECRET_KEY'] = '5e088df2bf772df379b5a0da138f2ebb'

posts = [
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


@app.route('/test')
def hello():
    return render_template('testpage.html')


@app.route("/")
@app.route('/home')
def home():
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
    # Access this registration form through an object of this class
    form = RegistrationForm()

    # When the form is submitted the current configs don't check very much the details about data fieldset
    # Here we shall include validated_on_submit() in order to avoid such issue
    if form.validate_on_submit():
        # output_success = 'Account created for user {}'.format('form.username.data')
        flash(f'Account created for {form.username.data} !', 'success')
        return redirect(url_for('home'))

    # And pass thi regitration form object to render_template() to include it's webelements
    return render_template('register.html', title='Register Here', form=form)

# Almost the same thing goes here (Same as register())
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login Form', form=form)


# @app.route("/test")
# def testpage():
#     return render_template('testpage.html', title='Test Page')


if __name__ == '__main__':
    app.run(debug=True)
