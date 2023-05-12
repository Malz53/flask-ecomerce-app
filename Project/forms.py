from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import Length, EqualTo, Email, DataRequired 

class RegisterForm(FlaskForm):
	username = StringField(label='User Name', validators=[Length(min=2, max=30), DataRequired()])
	email = StringField(label='Email Address' ,validators=[Email(), DataRequired()])
	pass1 = PasswordField(label = 'Enter Password', validators=[Length(min=6), DataRequired()])
	pass2 = PasswordField(label = 'Confirm Password' , validators=[EqualTo('pass1'), DataRequired()])
	submit = SubmitField(label = 'Create Account')

class UpdateForm(FlaskForm):
	
	username = StringField(label='User Name', validators=[Length(min=2, max=30), DataRequired()])
	email = StringField(label='Email Address' ,validators=[Email(), DataRequired()])
	pass1 = PasswordField(label = 'Enter New Password', validators=[Length(min=6), DataRequired()])
	pass2 = PasswordField(label = 'Confirm New Password' , validators=[EqualTo('pass1'), DataRequired()])
	pic = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
	submit = SubmitField(label = 'Update')

class Crud(FlaskForm):
	name = StringField(label='Product name')
	barcode = StringField(label='Barcode')
	price = StringField(label='Price')
	description = StringField(label='description')
	submit = SubmitField(label = 'Add item')


class Login(FlaskForm):
	username = StringField(label='User Name', validators=[DataRequired()])
	passw = PasswordField(label = 'Enter Password', validators=[DataRequired()])
	submit = SubmitField(label = 'Sign in :)')