from flask import  Blueprint, render_template, request, flash

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

    if request.method =='POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if password1 != password2: # password needs to match confirmation password
            flash("Passwords must match!", category='Error')
        else:
            flash("Account created", category="Success")

    return render_template("sign-up.html")

@auth.route('/home',)
def home():
    return render_template("home.html")

@auth.route('/userProfile', ) # routes to user Profile page; still need to test
def userProfile():
    name = "Christian Hernandez"
    vinylsSold = "241"
    followers = "841"

    return render_template("user-profile.html", name=name, vinylsSold=vinylsSold, followers=followers)

@auth.route('/editUserProfile') # routes to Profile editing page
def editUserProfile():
    return render_template("edit-user-profile.html")

