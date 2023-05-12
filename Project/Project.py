from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
class Item(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(length=50), nullable=False, unique=True)
	barcode = db.Column(db.String(length=12), nullable=False, unique=True)
	price = db.Column(db.Integer(), nullable=False)
	description = db.Column(db.String(1024), nullable=False, unique=True)

	def __repr__(self):
		return f'Item {self.name}'


@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/market')
def market():
	items = Item.query.all()
	return render_template('market.html', items=items)