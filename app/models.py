from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique=True)
    password_hash = db.Column(db.String(128))
    settings = db.Column(db.String(128))
    radius = db.Column(db.Integer(32))
    
    def __repr__(self):
        return f'<user: {self.username}>'  
