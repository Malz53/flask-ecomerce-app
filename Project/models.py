wsfrom Project import db, login_manager
from flask_login import UserMixin
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer(), primary_key=True)
	username = db.Column(db.String(length=30), nullable=False, unique=True)
	email_address = db.Column(db.String(length=50), nullable=False, unique=True)
	password_hash = db.Column(db.String(length=60), nullable=False)
	budget = db.Column(db.Integer(), nullable=False, default=10000)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	items = db.relationship('Item', backref='owned_user', lazy=True)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', {self.image_file}')"
	

class Item(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(length=50), nullable=False, unique=True)
	barcode = db.Column(db.String(length=12), nullable=False, unique=True)
	price = db.Column(db.Integer(), nullable=False)
	description = db.Column(db.String(2000), nullable=False, unique=True)
	owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

	def __repr__(self):
		return f'Item {self.name}'