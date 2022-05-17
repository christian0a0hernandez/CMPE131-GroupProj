from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_uploads import IMAGES, UploadSet, configure_uploads
from flask_msearch import Search

import os


basedir = os.path.abspath(os.path.dirname(__file__))
photos = UploadSet('photos', IMAGES)


db = SQLAlchemy()
DB_NAME = "database.db"

search = Search()


def create_app(): #initalizing flask
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '131project'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')
    configure_uploads(app, photos)

    db.init_app(app)
    search.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    create_database(app)

    from .models import User

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app

def create_database(app): # checks if database exists, if it doesn't make one
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print(("Database created."))
