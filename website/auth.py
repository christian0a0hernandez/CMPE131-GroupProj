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

@auth.route('/returnpolicy') # creates a page for return policy
def returnpolicy():
    return render_template("returnpolicy.html")
