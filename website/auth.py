from flask import  Blueprint, render_template, request

auth = Blueprint('a', __name__)

@auth.route('/login', methods=['GET', 'POST']) #create a log in page
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean = True)

@auth.route('/logout') # creates a page for log out
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST']) # creates a page for sign up
def sign_up():
    return render_template("sign-up.html")

@auth.route('/home',)
def home():
    return render_template("home.html")