from app import app, db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablname__ = 'users'
    
    id = db.Column(db.Integer(), primary_key = True)
    pin = db.Column(db.String(255))
    full_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    user_id = db.Column(db.String(255))
    pport_no = db.Column(db.String(255))