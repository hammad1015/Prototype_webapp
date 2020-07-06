from flask_login import UserMixin
from . import db

class User(db.Model, UserMixin):
    #Attribute Columns
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(75), unique=True) 
    username = db.Column(db.String(50), nullable=False) 
    password = db.Column(db.String(100), nullable=False) 
    #is_admin = db.Column(db.String(50), default=False)

    #A method used to check password during login 
    def check_password(self, password1):
    	return (True if password1 == self.password else False)

    #A method that returns the Primary key, This in used in the "load_user" function in routes.spy
    def get_id(self):
            #return (self.email).encode('utf-8')   #str.encode returns 'bytes' object
            return self.id

    #A method that prints the reffered user instance
    def __repr__(self):
        #return self
    	return "<User {}>".format(self.id)
    	#return f'Email: {self.email}, Username: {self.username}, Password: {self.password}'

class Buyer(db.Model):
    #Attribute Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), nullable=False)
    cnic = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text)

    #Relationships

    #This attribute would return the deal obect this buyer is associated to
    deal = db.relationship("Plot", backref='buyer_object', uselist=False)

class CommisionAgent(db.Model):
    #Attribute Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), nullable=False)
    cnic = db.Column(db.Integer, nullable=False)
    commission_rate = db.Column(db.Float, nullable=False)
    comments = db.Column(db.Text)

    #Relationships

    #This attribute returns a list of deals that  are associated to a particular agent, when called
    deals = db.relationship("Plot", backref='working_agent_object')

class Plot(db.Model):
    #Attribute Columns
    id = id =  db.Column(db.Integer, primary_key=True)
    adddress = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer)
    size = db.Column(db.String(20))
    status = db.Column(db.String(20), nullable=False)
    comments = db.Column(db.Text)

    #Relationships

    #This attribute would return the deal obect this plot is associated to
    deal = db.relationship("Plot", backref='plot_object', uselist=False)


class Deal(db.Model):
    #Attribute Columns
    id =                db.Column(db.Integer, primary_key=True)
    status =            db.Column(db.String(20), nullable=False)
    signing_date =      db.Column(db.String(20), nullable=False)
    comments =          db.Column(db.Text)

    #ForeginKey Columns
    working_agent_id =  db.Column(db.Integer, db.ForeginKey('commisionagent.id'), lazy=True)
    plot_id =           db.Column(db.Integer, db.ForeginKey('plot.id'), unique=True)
    buyer_id =          db.Column(db.Integer, db.ForeginKey('buyer.id'), unique=True)
    


