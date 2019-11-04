from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class food(FlaskForm):
    user_name = StringField('User Name', validators=[DataRequired()])
    pass_word = StringField('Password', validators=[DataRequired()])
    pass_word2 = StringField('Re-enter Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    register = SubmitField('Register')
    log_in = SubmitField('Log In')
    name = StringField('Name', validators=[DataRequired()])
    feedback = StringField('FeedBack',validators=[DataRequired()])
    submit = SubmitField('Submit')