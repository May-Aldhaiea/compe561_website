
"""
This deals with data entry. It takes care of the data entered by the user.
It takes care of the validation of the data and submission.

"""
#imports
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,ValidationError,Length, Email, EqualTo 
from wtforms import StringField,BooleanField,PasswordField,SubmitField

#SignUpForm
#Handles creation of a new account
#Validates the SignUp Data
class SignUpForm(FlaskForm):
     email = StringField('Email',validators=[DataRequired(), Email()])
     password = PasswordField('Password', validators=[DataRequired(),Length(min=5, max=255)])
     submit = SubmitField('Sign Up')
   
#SignInForm
#Handles user login
#Validates login data  
class SignInForm(FlaskForm):
     email = StringField('Email',validators=[DataRequired(), Email()])
     password = PasswordField('Password', validators=[DataRequired(),Length(min=5, max=255)])
     remember = BooleanField('Remember Me')
     submit = SubmitField('Sign In')