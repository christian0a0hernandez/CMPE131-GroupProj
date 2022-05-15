from flask_login import UserMixin
from sqlalchemy.sql import func

from . import db


class User(db.Model, UserMixin): # creates a user

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))


class Brand(db.Model): #creates a brand
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False,unique = True)

class Category(db.Model): #creates a category
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
