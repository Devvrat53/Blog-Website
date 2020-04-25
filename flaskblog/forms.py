from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username= StringField('Username', validators= [DataRequired(), Length(min= 2, max= 20)]) # to restrict username string between 2 to 20 characters
    email= StringField('Email', validators= [DataRequired(), Email()]) # 'Email()' validator validates whether the email is authentic or not!
    password= PasswordField('Password', validators= [DataRequired()])
    confirm_password= PasswordField('Confirm Password', validators= [DataRequired(), EqualTo('password')]) # 'EqualTo()' validator validates the password that the user inserts in password field
    submit= SubmitField('Sign Up')
    
class LoginForm(FlaskForm):
    email= StringField('Email', validators= [DataRequired(), Email()]) # 'Email()' validator validates whether the email is authentic or not!
    password= PasswordField('Password', validators= [DataRequired()])
    remember= BooleanField('Remember Me')
    submit= SubmitField('Login')
    
    