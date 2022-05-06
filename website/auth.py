from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import User, Brand, Category
from . import db
from .forms import Addproducts
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

    return render_template("login.html",user = current_user)

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


    return render_template("sign-up.html",user = current_user)

@auth.route('/home')
def home():
    return render_template("home.html",user = current_user)

@auth.route('/returnpolicy') # creates a page for return policy
def returnpolicy():
    return render_template("returnpolicy.html")

@auth.route('/delete', methods=['GET', 'POST']) # creates a page for deleting account
def delete_user():
    if request.method =='POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')

        user = User.query.filter_by(email = email).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            flash(f"Account deleted for, {firstName.title()}", category="Success")

        else:
            flash("No existing user found!", category='Error')
            return redirect(url_for('views.home'))
    return render_template("delete.html",user = current_user)

@auth.route('/userProfile') # routes to user Profile page; still need to test
def userProfile():
    name = "Christian Hernandez"
    vinylsSold = "241"
    followers = "841"
    return render_template("user-profile.html", name=name, vinylsSold=vinylsSold, followers=followers)

@auth.route('/editUserProfile') # routes to Profile editing page
def editUserProfile():
    return render_template("edit-user-profile.html")


@auth.route('/addbrand',methods = ['GET', 'POST'])
def addbrand():
    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'Brand "{getbrand}" added!','success')
        db.session.commit()
        return redirect(url_for('a.addbrand'))

    return render_template('addbrand.html',user = current_user,brands ='brands')

@auth.route('/addcategory',methods = ['GET', 'POST'])
def addcategory():
    if request.method == "POST":
        getbrand = request.form.get('category')
        category = Category(name=getbrand)
        db.session.add(category)
        flash(f'Category "{getbrand}" added!','success')
        db.session.commit()
        return redirect(url_for('a.addbrand'))

    return render_template('addbrand.html',user = current_user)

@auth.route('/addproduct', methods =['POST','GET'])
def addproduct():
    form = Addproducts(request.form)
    return render_template('addproduct.html', title ="Add Product", form = form,user = current_user)

