from os import environ

class Config:
    
    FLASK_APP           = 'wsgi.py'
    SECRET_KEY          = 'secret key' #environ.get("FlaskPrototypeSecretKey")
    STATIC_FOLDER       = 'static'
    TEMPLATES_FOLDER    = 'templates'

    
class DevelopmentConfig(Config):
    
    ENV                     = 'Development' #environ.get('FlaskPrototypeDevEnv')
    DEBUG                   = True
    TESTING                 = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/build_guild' #environ.get('FlaskPrototypeDevDB')

    
class ProductionConfig(Config):
    
    ENV                         = environ.get('FlaskPrototypeProdEnv')
    DEBUG                       = False
    TESTING                     = False
    #SQLALCHEMY_DATABASE_URI    = # production db uri string #
