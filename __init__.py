from flask import Flask #import flask to create object
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #myFlaskObj has been created
app.config.from_object(Config)

db = SQLAlchemy(app)

from application import routes, models