import json
import os


def file_path() -> str:
    filepath = os.path.abspath('flaskblog/config_vars/config.json')
    print(f'Found file path for config.json: {filepath}')
    return filepath


with open(file_path()) as config_file:
    config = json.load(config_file)


class Config:
    # Add a secret key to Application, in order to protect against Xss and hacks
    # Generated from python3 secrets module with token_hex(some int value)
    SECRET_KEY = config.get('SECRET_KEY')
    # To work wit DB, we'd use sqlite db
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')

    # SMTP Configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # the gmail account's username and password is better being hidden
    # The required data is good to have in environment variables or some encrypted config file on server.
    # for now let's just use the environment variables
    MAIL_USERNAME = config.get('TEST_EMAIL_USER')
    MAIL_PASSWORD = config.get('TEST_EMAIL_PASS')
