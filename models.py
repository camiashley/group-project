from application import db
from datetime import datetime
from flask import Flask, render_template, url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, 
nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash= db.Column(db.String(100), unique=True, 
nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)


    def __repr__(self):
       return f"user('{self.username}','{self.email}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(120), nullable=False)
    timestamps = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

def __repr__(self):
       return f"post('{self.body}')"