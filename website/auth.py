from flask import  Blueprint

auth = Blueprint('a', __name__)

@auth.route('/login') #create a log in page
def login():
    return "<p>Login</p>"

@auth.route('/logout') # creates a page for log out
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up') # creates a page for sign up
def sign_up():
    return "<p>Sign up</p>"