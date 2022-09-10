from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, email_validator, Email, ValidationError
from first_web.model import User
from flask_wtf.file import FileField, FileAllowed

class RegistrationForm(FlaskForm):
    username= StringField('Username', validators=[DataRequired(),Length(max=20, min=5)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password= PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit= SubmitField('Sign Up')

    def validate_username(self,username):
        user= User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken try new')
    def validate_email(self,email):
        user= User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already taken try new')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password= PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit= SubmitField('Sign Up')


class UpdateAccountForm(FlaskForm):
    username= StringField('Username', validators=[DataRequired(),Length(max=20, min=5)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture= FileField('Update prfoile picture', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit= SubmitField('UPDATE')

    def validate_username(self,username):
        if username.data != current_user.username:
            user= User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is already taken try new')

    def validate_email(self,email):
        if email.data != current_user.email:
            user= User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is already taken try new')


class PostForm(FlaskForm):
    title= StringField('Title', validators=[DataRequired()])
    content= TextAreaField('Content', validators=[DataRequired()])
    submit= SubmitField('Post')


