#!/usr/bin/env python3

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, DataRequired, Email, EqualTo


# For Registering the users in blog
class RegistrationForm(FlaskForm):
    # Username, Email etc... are  the label for the form
    # With some level of Validation by this class
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])

    # DataRequired() and Email() are the build in validators in wfforms madule
    # You'd need to just call them with the respective field
    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    # For now keeping only DataRequired() as a validator
    # Later will add constraints for min and max length.
    password = PasswordField('Password',
                             validators=[DataRequired()])
    # password and confirm_password must match. So using EqualTo validator function.
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    # Add a form submit element
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    # Username, Email etc... are  the label for the form
    # With some level of Validation by this class
    # username = StringField('Username',
    #            validators=[DataRequired(),Length(min=2,max=20)])

    # DataRequired() and Email() are the build in validators in wfforms madule
    # You'd need to just call them with the respective field
    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    # For now keeping only DataRequired() as a validator
    # Later will add constraints for min and max length.
    password = PasswordField('Password',
                             validators=[DataRequired()])
    # password and confirm_password must match. So using EqualTo validator function.
    # confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])

    # Adding a remmeber me option
    remmeber = BooleanField('Remember Me...')

    # Add a form submit element
    submit = SubmitField('Login')
