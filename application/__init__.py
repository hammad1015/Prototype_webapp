from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#import configfile

db = SQLAlchemy()
#login_manager = LoginManager()

def create_app():
    """ Creating the Flask app and setting its config """

    #Creating the flask app
    app = Flask(__name__, instance_relative_config=False)

    #setting config variables from DevelopmentConfig class in config file
    app.config.from_object('config.DevelopmentConfig')

    #Initiaizaing Plugins
    db.__init__(app)
    #login_manager.__init__(app)

    with app.app_context():

        #Incuding Routes
        from . import routes

        #Creating tables in the database
        #db.create_all()

        #print(app.config)

        return app
    
    
