# Vinyl Hill Website #
## Team Members ##
* __Team Lead__: Steven Stansberry (@stevenpstansberry)
* Christian Hernandez (@christian0a0hernandez)
* Joseph Guzman (@Josephtheelder)
* Inderpreet Singh (@Singh1309)
## About ##
This purpose of this website program is for Vinyl enthusiasts & collectors to buy and sell vinyl records. 

### Functional Requirments and their contributors ###
* Steven Stansberry - Login, create new account, stock check          
* Christian Hernandez - My shopping cart, my wish list, user profiles   
* Joseph Guzman - Return policy, user reviews                     
* Inderpreet Singh - Delete account, search bar, discount promotions 
   
### Non Functional Requirments ###
There are 4 non- functional requirments: 
* Dark mode
* Interactve user interface with simple design
* Ability to run on multiple browsers
* Low latency/fast performance

## Install the following packages using the linux command in your terminal ##

`pip install flask`
`pip install flask-login`
`pip install flask-sqlalchemy`
`pip install flask-wtf`
`pip install flask_uploads`
`pip install Werkzeug`
`pip install Flask-Reuploaded`

##  Installtion & Setup  ##
Install the program into your system using the following linux command: 
`git clone <repo-url>`

Make sure you have the latest version of Python and select it as the programs interperter once the program is installed ( Version 3.8  or above)

## Running The App ##
`python main.py`

## Viewing The App ##
Go to `http://127.0.0.1:5000` on your web browser

# Tutorial 

### Sign Up
In order for users to create an account on the site they must enter the required information.
Users need to add their email, name, and password in order to successfully sign up. 
It will ask the user to confirm passwords co they must match the first one you entered.

### Login
For users to log in all they need to do is type their information they inputted at sign up correctly. 
The site will then direct you to the home page under your account.

### Delete Account
Users can delete their account by clicking the option at the top of the website.
From this page they need to type their email and if it matches one in our database then it will successfully delete the account.
If the email was not there then it cannot complete the deletion.

### Products
The three functions of adding a product, brand, or category are all relatively similar to complete.
They first can be accessed at the top of the website through the navigation bar. 
Each page will require the user to input information depending on what they want to add.

For example, in order for a user to add a product, they first have to hit the link at the top of the page named "Add a Product".
There they will have to add information about the name, price, discount, genre, artist, stock, and description of the vinyl.
After they have put in the correct information, all they need to do is click on the "Add" button at the bottom of the page.

### Account Management
Users can view their profile by clicking the option "View Profile" at the top of the website. 
Here they can see their recent vinyls and reviews.

When users are on the profile page and hit the "Edit" button they can change their information.
On that page the user just has to input in the text boxes of what they want to change.
They can change their first name, username, email, and password.
Once they are done they need to hit the "Save Profile" button at the bottom of the page.
This will take them back to the profile page with updated information.
