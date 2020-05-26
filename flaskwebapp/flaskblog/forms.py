#!/usr/bin/env python3

from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flaskblog.models import User
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import Length, DataRequired, Email, EqualTo, ValidationError


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

    def validate_username(self, username):
        # Validate if user already exists in DB with this Username
        user = User.query.filter_by(username=username.data).first()
        # Possible value of user variable other than username would be None, in that case condition isn't satisfied.
        if user:
            # if the user exists who is registering then raise the Validation error
            raise ValidationError(f'Username "{username.data}" is already taken! Please use different Username for '
                                  f'registration.')

    def validate_email(self, email):
        # Validate if user already exists in DB with this email
        user_email = User.query.filter_by(email=email.data).first()
        # Possible value of user variable other than username would be None, in that case condition isn't satisfied.
        if user_email:
            # if the user exists who is registering then raise the Validation error
            raise ValidationError(f'Email ID "{email.data}" is already taken ! Please use different Email ID')


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
    remember = BooleanField('Remember Me...')

    # Add a form submit element
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update profile picture', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    f'Username "{username.data}" is already taken! Please use different Username for registration.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user_email = User.query.filter_by(email=email.data).first()
            if user_email:
                raise ValidationError(f'Email ID "{email.data}" is already taken ! Please use different Email ID')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user_email = User.query.filter_by(email=email.data).first()
        if user_email is None:
            raise ValidationError(
                f'Email ID "{email.data}" is NOT registered with any account !'
                f' Please use correct Email ID or create a new account')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password')
