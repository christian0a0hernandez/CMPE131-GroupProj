from flask import  Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('a', __name__)

@auth.route('/login', methods=['GET', 'POST']) #create a log in page
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                flash('Logged in!', category= 'Success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password.", category="Error")
        else:
            flash("Email doesn't exist", category='error')

    ##data = request.form
    ##print(data)
    return render_template("login.html")

@auth.route('/logout') # creates a page for log out
def logout():
    logout_user()
    return redirect(url_for('a.home'))

@auth.route('/sign-up', methods=['GET', 'POST']) # creates a page for sign up
def sign_up():
    if request.method =='POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email = email).first()
        if user:
            flash("Email already exists")

        elif password1 != password2: # password needs to match confirmation password
            flash("Passwords must match!", category='Error')
        else:
            new_user = User(email=email, firstName = firstName, password = password1)
            db.session.add(new_user)
            db.session.commit()
            flash(f"Thanks for registering, {firstName.title()}", category="Success")
            return redirect(url_for('views.home'))


    return render_template("sign-up.html")

@auth.route('/home')
def home():
    return render_template("home.html")

@auth.route('/returnpolicy') # creates a page for return policy
def returnpolicy():
    return render_template("returnpolicy.html")

@auth.route('/userProfile') # routes to user Profile page; still need to test
def userProfile():
    name = "Christian Hernandez"
    vinylsSold = "241"
    followers = "841"
    return render_template("user-profile.html", name=name, vinylsSold=vinylsSold, followers=followers)

@auth.route('/editUserProfile') # routes to Profile editing page
def editUserProfile():
    return render_template("edit-user-profile.html")