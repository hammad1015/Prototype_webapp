from flask_login import UserMixin
from . import db

class User(db.Model, UserMixin):
    #id = db.Column(db.Integer, primary_key=True) 
    id = db.Column(db.String(75), primary_key=True) 
    username = db.Column(db.String(50), nullable=False) 
    password = db.Column(db.String(100), nullable=False) 
    #is_admin = db.Column(db.String(50), default=False)

    #A method used to check password during login 
    def check_password(self, password1):
    	return (True if password1 == self.password else False)

    #A method that returns unicode for the Primary key, This i used in the "load_user" function in routes.spy
    #def get_id(self):
    #        return (self.email).encode('utf-8')

    #A method that prints the reffered user instance
    def __repr__(self):
    	return '<User {}>'.format(self.username)
    	#return f'Email: {self.email}, Username: {self.username}, Password: {self.password}'

