from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from app import form

class LoginForm(FlaskForm):
    UserName = StringField('UserName')
    Password = Password('City rank')
    Remember_me = BooleanField('Remember me')
    comments = StringField('comments')
    submit = SubmitField('Sign In')
