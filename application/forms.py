from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextField
from wtforms.validators import DataRequired, Length

#Login Form 
class LoginForm(FlaskForm):
    email    = StringField('Email', validators=[DataRequired(), Length(min=1, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=1, max=25)])
    submit   = SubmitField('Login')

#Create Buyer Form
class CreateBuyerForm(FlaskForm):
	id 	 	 = IntegerField('Buyer ID', validators=[DataRequired()])
	name 	 = StringField('Name', validators=[DataRequired(), Length(min=1, max=75)])
	cnic 	 = IntegerField('CNIC', validators=[DataRequired()])
	comments = TextField('Comments', validators=[])
	submit 	 = SubmitField('Create Buyer')
