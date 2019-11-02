import os
basedir = os.path.abspath(os.path.dirname(__name__))
 
class Config():
    SECRET_KEY = 'oops'
    SQLALCHEMY_DATABASE_URL = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = false
