from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField, HiddenField, SelectField
from wtforms.validators import DataRequired, Length, number_range

from .model import Plot

#Login Form 
class LoginForm(FlaskForm):
	
    email    = StringField  ('Email'   , validators=[DataRequired(), Length(min=1, max=75)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=1, max=100)])
    submit   = SubmitField  ('Login')

#Add Buyer Form
class AddBuyerForm(FlaskForm):

	#id 	 = IntegerField('Buyer ID', validators=[DataRequired()])
	name 	 = StringField  ('Name'    , validators=[DataRequired(), Length(min=1, max=75)])
	cnic 	 = IntegerField ('CNIC'    , validators=[DataRequired(), number_range(min=1)])
	comments = TextAreaField('Comments', validators=[])
	submit 	 = SubmitField  ('Create Buyer')


#Edit Buyer Info Form
class EditBuyerForm(FlaskForm):
	name 	 = StringField  ('Name'    , validators=[DataRequired(), Length(min=1, max=75)])
	cnic 	 = IntegerField ('CNIC'    , validators=[DataRequired(), number_range(min=1)])
	comments = TextAreaField('Comments', validators=[])
	submit 	 = SubmitField  ('Edit Buyer')

	
#Search Buyer Form
class SearchBuyerForm(FlaskForm):

	id     = IntegerField('Buyer ID')
	name   = StringField ('Name')
	search = SubmitField ('Search Buyer')


#Delete Buyer Form
class DeleteBuyerForm(FlaskForm):

	id     = HiddenField('buyer_id')
	delete = SubmitField('Delete Buyer')

#Add Deal Form 
class AddDealForm(FlaskForm):

	#id 						= IntegerField('Deal ID', validators=[DataRequired()])
	buyer_id 				= IntegerField  ('Buyer ID'              , validators=[DataRequired()])
	plot_id 				= IntegerField  ('Plot ID'               , validators=[DataRequired()])
	first_amount_recieved 	= IntegerField  ('First Paid Amount'     , validators=[DataRequired()])
	amount_per_installment 	= IntegerField  ('Amount per Installment', validators=[DataRequired()])
	installment_frequency 	= StringField   ('Installments per Year' , validators=[DataRequired()])
	comments 				= TextAreaField ('Comments'              , validators=[])
	submit 					= SubmitField   ('Create Deal')

# Add Transaction Form
class AddTransactionForm(FlaskForm):

    pass

# Add Notes Form
class AddNotesForm(FlaskForm):

	title   = StringField  ('Title',  validators=[DataRequired()])
	content = TextAreaField('Content')
	add 	= SubmitField  ('Add Note')

#Add Buyer Form
class AddNormalUserForm(FlaskForm):

	#id 	 = IntegerField('Buyer ID', validators=[DataRequired()])
	username = StringField('Username',   validators=[DataRequired(), Length(min=1, max=50)])
	email    = StringField('Email',      validators=[DataRequired(), Length(min=1, max=75)])
	password = PasswordField('Password', validators=[Length(max=100)], default='12345')
	create 	 = SubmitField('Create User')

#Set Plot Price Form
class SetPlotPrice(FlaskForm):
	
	address = SelectField('Address', choices=[row[0] for row in Plot.query.with_entities(Plot.address).all()])
	price   = IntegerField('Price',  validators=[DataRequired()])
	set     = SubmitField('Set Price')

#Add Expenditure Type Form
class AddExpendituretypeForm(FlaskForm):

	name = StringField('Name of Expenditure', validators=[DataRequired(), Length(min=1, max=100)])
	add  = SubmitField('Add Expenditure Type')

# search form
class SearchForm(FlaskForm):

    value  = StringField('Value', validators= [DataRequired()])
    search = SubmitField('Search')


#Filter Plot by Status Form
class FilterPlotForm(FlaskForm):

	status = SelectField('Filter By:', choices=[('all', 'All'), ('sold','Sold'), ('not sold','Not Sold'), ('in a deal','In a Deal')])
	filter = SubmitField('Filter')


#Add Transaction Form
class AddTransactionForm(FlaskForm):
	
	deal_id  = HiddenField('deal_id')
	exp_id   = HiddenField('exp_id')
	amount   = IntegerField('Amount', validators=[DataRequired(), number_range(min=0)])
	comments = TextAreaField('Comments')
	add      = SubmitField('Enter Payment')
