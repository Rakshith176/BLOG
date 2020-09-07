from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Length, Email, EqualTo
#from email_validator import email_validator

class RegistrationForm(FlaskForm):
    
    username = StringField('Username',validators=[Length(min=4, max=25),DataRequired()])
    email = StringField('Email', validators=[Length(min=6, max=35),Email()])
    password = PasswordField('New Password', validators=[DataRequired(),Length(min=8,max=20)])
    confirm_password = PasswordField('Confirm Password',validators=[EqualTo('password'),DataRequired()])
    submit= SubmitField('Signup')

 
class LoginForm(FlaskForm):
    
    email = StringField('Email Address', validators=[Length(min=6, max=35),Email()])
    password = PasswordField('Password',  validators=[DataRequired(),Length(min=8, max=20)])
    submit= SubmitField('Login')    