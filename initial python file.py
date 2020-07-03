#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy



#app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Cforcat.001@localhost:3306/test'
#db = SQLAlchemy(app)
#app.secret_key = 'shhhh...iAmASecret!'

#class User(db.Model):
 #   id = db.Column(db.Integer, primary_key=True) 
 #   email = db.Column(db.String(75)) 
 #   username = db.Column(db.String(50)) 
 #   password = db.Column(db.String(100)) 
 #   is_admin = db.Column(db.String(50), default=False)

#@app.route("/", methods=['GET'])
#def home():
#    return '<b>HOME</b>'

