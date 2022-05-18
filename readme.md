# Vinyl Hill Website #
## About ##
Vinly Hill is a website that enables music enthusiasts to buy and sell vinyls at the comfort of their home.
The websites user services allows users to create new profiles, login as existing user, edit profiles, search 
for products, checkout products,manage inventory, add products, add artists and add categories. The website is 
developed by utilizing the flask platform and using the python programming language with HTML as well. It uses 
a database system to store & edit various types of products and user profiles. 
# Software Functionality # 
## Homepage ##
(image)
Upon accessing the website, the top of the homepage has a taskbar directory that allows you to navigate through
various pages built within the website. The middle of the page has several hyperlinks that direct you to our category,
contact and promotional page. The bottom of the home page has a description of the developers behind this website. 

## Signup ##
(image)
Our signup page is easy and simple enough for new users to create a profile on our website and get started! The page 
requires new users to input their email address, first name and password. If you try to create an account with 
an email address from an existing profile, it will not let you.

## Inventory ##
(Image) 
Once you are logged in, select the store page where you will see the products we have for sale. The inventory catalog
can be updated by users who wish to sell their own vinyls!

## Add product ##
(image)
The add product page allows users to list their vinyls for sale hassle free! Our user-friendly design makes it easy enough
for new product listings to include the name, price, discount, genre,artist, stock and a description of the listing. 

## Promotional page ##
(image) 
The website offers various promitional deals for buying customers. Simply use the promo code in the check out page.  

## Checkout ##
(image)
Our checkout page allows you to input your personal information for shipping and payment options. Enter the promocode to 
reveive a discount off your order!









## Team Members ##
* __Team Lead__: Steven Stansberry (@stevenpstansberry)
* Christian Hernandez (@christian0a0hernandez)
* Joseph Guzman (@Josephtheelder)
* Inderpreet Singh (@Singh1309) 

### Functional Requirments and their contributors ###
* Steven Stansberry - Login, create new account, stock check          
* Christian Hernandez - My shopping cart, my wish list, user profiles   
* Joseph Guzman - Return policy                   
* Inderpreet Singh - Delete account, search bar, discount promotions, homepage, checkout, support page
   
### Non Functional Requirments ###
There are 4 non- functional requirments: 
*Meet the team github accounts.
*Interactive User Interface with simple design -Christian
*Will be able to work on multiple browsers
*Low latency/Fast Performance ideally response time of ~ 1ms
*Sliding sections on the homepage.

## Install the following packages using the linux command in your terminal ##

`pip install flask`
`pip install flask-login`
`pip install flask-sqlalchemy`
`pip install flask-wtf`
`pip install flask_uploads`
`pip install Werkzeug`
`pip install Flask-Reuploaded`
`pip install flask-msearch`
`pip install pandas`


##  Installtion & Setup  ##
Install the program into your system using the following linux command: 
`git clone <repo-url>`

Make sure you have the latest version of Python and select it as the programs interperter once the program is installed ( Version 3.8  or above)

## Running The App ##
`python main.py`

## Viewing The App ##
Go to `http://127.0.0.1:5000` on your web browser
