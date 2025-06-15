from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

user_hobbies = db.Table('user_hobbies',
	db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
	db.Column('hobby_id', db.Integer, db.ForeignKey('hobby.id'), primary_key=True),
)

class Hobby(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True, nullable=False)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(150), unique=True, nullable=False)
	password = db.Column(db.String(150), nullable=False)
	email = db.Column(db.String(150), unique=True, nullable=False)
	
	hobbies = db.relationship('Hobby', secondary=user_hobbies, backref='users')

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return str(self.id)