import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# To protect the app against of false logins
from flask_bcrypt import Bcrypt
# to manage the user login
from flask_login import LoginManager
# To send emails from application to users
from flask_mail import Mail
#Use the config.py to import configurations
from flaskblog.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'  # name of the function that handles /login req(s)
# login_manager.login_message = 'Please log in to access this view.'
login_manager.login_message_category = 'info'  # Just adding nice blue colored category from bootstrap

# now initialize these to mail
mail = Mail()


# To create multiple instances of the application,
# it is better to have some function that can externalize the app
# To all of the above extensions, we'd pass the app from this functions,
# Reason: on the fly, every new instance whenever externalized, will get those extensions at runtime for themselves.
def create_app(config_class=Config):
    # Initialize this App to FlaskApp
    app = Flask(__name__)

    # Pass config object to app
    app.config.from_object(config_class)

    # Assign extensions here for every instance of this application
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # CRITICAL Blueprints!!
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    # Now register the blueprints with application 'app'
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    # When created return the application instance
    return app


