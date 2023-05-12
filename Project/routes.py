import secrets
import os
from Project import app
from flask import render_template, redirect, url_for, flash, request
from Project.models import Item, User
from Project.forms import RegisterForm, Login, UpdateForm, Crud
from Project import db
from flask_login import login_user, logout_user, current_user

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/market')
def market():
	items = Item.query.all()
	return render_template('market.html', items=items)

@app.route('/register', methods=['GET','POST'])
def registration_page():
	form = RegisterForm()
	if form.validate_on_submit():
		user_to_create = User(username=form.username.data, 
							  email_address=form.email.data, 
							  password_hash=form.pass1.data)
		db.session.add(user_to_create)
		db.session.commit()
		return redirect(url_for('market'))
	if form.errors !={}:
		for err_msg in form.errors.values():
			flash(f'There was an error with creating a user: {err_msg}')	
	return render_template('regpage.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
	form = Login()
	if form.validate_on_submit():
		attempted_user = User.query.filter_by(username=form.username.data).first()
		attempted_passw = User.query.filter_by(password_hash=form.passw.data).first()
		if attempted_user and attempted_passw: 
			login_user(attempted_user)
			flash('Success! Your are logged in', category='success')
			return redirect(url_for('market'))
		else:
			flash('Username and password do no match! Please try agaon :)', category='danger')

	return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
	logout_user()
	flash("You have logged out", category='info')
	return redirect(url_for('home'))

def save_pic(form_pic):
	random_hex=secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_pic.filename)
	pic_fn = random_hex + f_ext
	pic_path = os.path.join(app.root_path, 'static/profile_pics', pic_fn)
	form_pic.save(pic_path)

	return pic_fn

@app.route('/profile', methods=['POST', 'GET'])
def profile_page():
	form = UpdateForm()
	if form.validate_on_submit():
		if form.pic.data:
			pic_file = save_pic(form.pic.data)
			current_user.image_file = pic_file
		current_user.username = form.username.data
		current_user.email_address = form.email.data
		current_user.password_hash = form.pass1.data

		db.session.commit()
		flash('your account has been updated!', 'success')
		return redirect(url_for('profile_page'))
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.email.data = current_user.email_address
		form.pass1.data = current_user.password_hash
		form.pass2.data = current_user.password_hash

	image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
	
	return render_template('profile.html', image_file=image_file, form=form)

@app.route('/CRUD', methods=['POST', 'GET'] )
def crud_page():
	form = Crud()
	if form.validate_on_submit():
		item_to_create = Item(name=form.name.data, 
							  price=form.price.data, 
							  barcode=form.barcode.data,
							  description=form.description.data)
		db.session.add(item_to_create)
		db.session.commit()
		return redirect(url_for('market'))
	return render_template('CRUD.html', form=form)