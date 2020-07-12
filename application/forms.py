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
	
	id 	 = IntegerField('Buyer ID', validators=[DataRequired()])
	name 	 = StringField('Name', validators=[DataRequired(), Length(min=1, max=75)])
	cnic 	 = IntegerField('CNIC', validators=[DataRequired()])
	comments = TextField('Comments', validators=[])
	submit 	 = SubmitField('Create Buyer')


#Create Deal Form 
class CreateDealForm(FlaskForm):
	
	id 			= IntegerField('Deal ID', validators= [DataRequired()])
	buyer_id 		= IntegerField('Buyer ID', validators= [DataRequired()])
	plot_id 		= IntegerField('Plot ID', validators= [DataRequired()])
	first_amount_recieved 	= IntegerField('First Paid Amount', validators= [DataRequired()])
	amount_per_installment 	= IntegerField('Amount per Installment', validators= [DataRequired()])
	installment_frequency 	= StringField ('Installments per Year', validators= [DataRequired()])
	comments 		= TextField   ('Comments', validators= [])
	submit 			= SubmitField ('Create Deal')
