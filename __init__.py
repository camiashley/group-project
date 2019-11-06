from flask import Flask #import flask to create object
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__) #myFlaskObj has been created
app.config.from_object(Config)

db = SQLAlchemy(app)    #create the db object represent the database
migrate = Migrate(app, db)  #create the migrate object

from application import routes, models