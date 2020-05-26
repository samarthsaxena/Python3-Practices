import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# To protect the app against of false logins
from flask_bcrypt import Bcrypt
# to manage the user login
from flask_login import LoginManager
# To send emails from application to users
from flask_mail import Mail

# Initialize this App to FlaskApp
app = Flask(__name__)

# Add a secret key to Application, in order to protect against Xss and hacks
# Generated from python3 secrets module with token_hex(soem int value)
app.config['SECRET_KEY'] = '5e088df2bf772df379b5a0da138f2ebb'
# To work wit DB, we'd use sqlite db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # name of the function that handles /login req(s)
# login_manager.login_message = 'Please log in to access this view.'
login_manager.login_message_category = 'info'  # Just adding nice blue colored category from bootstrap

# SMTP Configurations
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
# the gmail account's username and password is better being hidden
# The required data is good to have in environment variables or some encrypted config file on server.
# for now let's just use the environment variables
app.config['MAIL_USERNAME'] = os.environ.get('TEST_EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('TEST_EMAIL_PASS')

# now initialize these to mail
mail = Mail(app)

# CRITICAL !!
from flaskblog import routes
