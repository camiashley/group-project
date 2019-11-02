from flask import Flask
from config import Config
from flask_sqlalchemy import flask_sqlalchemy
myFlaskObj = Flask(__name__)
myFlaskObj.config.from_object(Config)

db = SQLAlchemy(myFlaskObj)

from app import localfoodie, models
