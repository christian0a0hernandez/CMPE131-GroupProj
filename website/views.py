from os import abort

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from werkzeug.utils import redirect

from website import db
from website.models import User

views = Blueprint('views', __name__)

@views.route('/')
def home ():
    return render_template("home.html")


