from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin

from flask_admin.base import MenuLink

from .adminviews import AdminPanel, ProtectedModelView

db            = SQLAlchemy()
login_manager = LoginManager()
admin         = Admin()

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

        from . import model

        #Creating tables in the database
        # db.drop_all()
        # db.create_all()

        #Adding Dummy Data
        # db.session.add(model.User(id=1, username="Faisal Rasool", email="faisal@example.com",  password="pop", rank=0))
        # db.session.add(model.User(id=2, username="Abdul Rafey",   email="rafey@example.com",   password="pop", rank=0))
        # db.session.add(model.User(id=3, username="Manager 1",     email="manager@example.com", password="pop", rank=1))

        # db.session.add(model.Plot(id=1, type="residential", address="first",  status="not sold", size="7"))
        # db.session.add(model.Plot(id=2, type="residential", address="second", status="not sold", size="2"))
        # db.session.add(model.Plot(id=3, type="residential", address="third",  status="not sold", size="5"))
        # db.session.add(model.Plot(id=4, type="residential", address="fouth",  status="not sold", size="5"))
        # db.session.add(model.Plot(id=5, type="residential", address="fifth",  status="not sold", size="7"))
        # db.session.add(model.Plot(id=6, type="residential", address="sixth",  status="not sold", size="5"))
        # db.session.add(model.Plot(id=7, type="residential", address="seventh",status="not sold", size="7"))
        # db.session.add(model.Plot(id=11, type="commercial", address="eleven", status="not sold", size="5"))
        # db.session.add(model.Plot(id=12, type="commercial", address="twelve", status="not sold", size="5"))
        # db.session.add(model.Plot(id=13, type="commercial", address="thirteen", status="not sold", size="5"))
        # db.session.add(model.Plot(id=14, type="commercial", address="fourteen", status="not sold", size="5"))
        # db.session.add(model.Plot(id=15, type="commercial", address="fifteen",  status="not sold", size="5"))
        # db.session.add(model.Plot(id=16, type="commercial", address="sixteen",  status="not sold", size="5"))
        # db.session.commit()

        #Addning Databse Views to Admin Panel
        admin.add_view(ProtectedModelView(model.User,  db.session, category='Databases', name="Users"))
        admin.add_view(ProtectedModelView(model.Buyer, db.session, category='Databases', name="Buyers"))
        admin.add_view(ProtectedModelView(model.Deal,  db.session, category='Databases', name="Deals"))
        admin.add_view(ProtectedModelView(model.Plot,  db.session, category='Databases', name="Plots"))
        admin.add_view(ProtectedModelView(model.Notes, db.session, category='Databases', name="Notes"))
        admin.add_view(ProtectedModelView(model.Transaction, db.session, category='Databases', name="Transactions"))
        admin.add_link(MenuLink(name='Back to Profile', url='/profile'))

        #Incuding Routes
        from . import routes

        return app   
