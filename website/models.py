from flask_login import UserMixin
from sqlalchemy.sql import func

from . import db


<<<<<<< Updated upstream
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
=======
class User(db.Model, UserMixin): # creates a user
>>>>>>> Stashed changes
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
<<<<<<< Updated upstream
    notes = db.relationship('Note')
=======

class Brand(db.Model): #creates a brand
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False,unique = True)

class Category(db.Model): #creates a category
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)

>>>>>>> Stashed changes
