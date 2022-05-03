from flask_sqlalchemy import SQLAlchemy
from flask_whooshalchemy import whoosh_index
from website import app

db = SQLAlchemy()

class User(db.model):
  __searchable__ = ['name']
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64))

whoosh_index(app, User)