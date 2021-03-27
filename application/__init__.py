from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin

from flask_admin.contrib.sqla import ModelView
from flask_admin.base import MenuLink

from .adminindexview import AdminPanel
#from .model import User, Buyer, Deal, Plot, Transaction, Notes

db            = SQLAlchemy()
login_manager = LoginManager()
admin  = Admin()

def create_app():
    """ Creating the Flask app and setting its config """

    #Creating the flask app
    app = Flask(__name__, instance_relative_config=False)

    #setting config variables from DevelopmentConfig class in config file
    app.config.from_object('config.DevelopmentConfig')

    #Initiaizaing Plugins
    db.__init__(app)
    login_manager.__init__(app)
    admin.init_app(app, index_view=AdminPanel(name="Admin Panel"))

    with app.app_context():

        #Incuding Routes
        from . import routes

        #Addning Databse tables to Admin Panel
        admin.add_view(ModelView(model.User,  db.session, category='Databases', name="Users"))
        admin.add_view(ModelView(model.Buyer, db.session, category='Databases', name="Buyers"))
        admin.add_view(ModelView(model.Deal,  db.session, category='Databases', name="Deals"))
        admin.add_view(ModelView(model.Plot,  db.session, category='Databases', name="Plots"))
        admin.add_view(ModelView(model.Notes, db.session, category='Databases', name="Notes"))
        admin.add_view(ModelView(model.Transaction, db.session, category='Databases', name="Transactions"))
        admin.add_link(MenuLink(name='Back to Profile', url='/profile'))

        #Creating tables in the database
        #db.drop_all()
        #db.create_all()

        #print(app.config)

        return app   
