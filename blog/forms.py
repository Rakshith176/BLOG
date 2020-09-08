from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Length, Email, EqualTo,ValidationError
from blog.models import User
 
class RegistrationForm(FlaskForm):
    
    username = StringField('Username',validators=[Length(min=4, max=25),DataRequired()])
    email = StringField('Email', validators=[Length(min=6, max=35),Email()])
    password = PasswordField('New Password', validators=[DataRequired(),Length(min=8,max=20)])
    confirm_password = PasswordField('Confirm Password',validators=[EqualTo('password'),DataRequired()])
    submit= SubmitField('Signup')
    def validate_username(self,username):
    	user = User.query.filter_by(username=username.data).first()
    	if user:
    		raise ValidationError('The username is taken. Choose different username')
    def validate_email(self,email):
    	user = User.query.filter_by(email=email.data).first()
    	if user:
    		raise ValidationError('The email is taken. Choose different email')



 
class LoginForm(FlaskForm):
    
    email = StringField('Email Address', validators=[Length(min=6, max=35),Email()])
    password = PasswordField('Password',  validators=[DataRequired(),Length(min=8, max=20)])
    remember =BooleanField('Remember Me')
    submit= SubmitField('Login')    