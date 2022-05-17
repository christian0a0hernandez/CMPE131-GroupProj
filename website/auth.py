from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import User, Brand, Category, Addproduct
from . import db, photos
from .forms import Addproducts
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('a', __name__)


@auth.route('/login', methods=['GET', 'POST'])  # create a log in page
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                flash('Logged in!', category='Success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password.", category="Error")
        else:
            flash("Email doesn't exist", category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')  # creates a page for log out
def logout():
    logout_user()
    return redirect(url_for('a.home'))


@auth.route('/sign-up', methods=['GET', 'POST'])  # creates a page for sign up
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists")

        elif password1 != password2:  # password needs to match confirmation password
            flash("Passwords must match!", category='Error')
        else:
            new_user = User(email=email, firstName=firstName, password=password1)
            db.session.add(new_user)
            db.session.commit()
            flash(f"Thanks for registering, {firstName.title()}", category="Success")
            return redirect(url_for('views.home'))

    return render_template("sign-up.html", user=current_user)


@auth.route('/home')
def home():
    return render_template("home.html", user=current_user)


@auth.route('/returnpolicy')  # creates a page for return policy
def returnpolicy():
    return render_template("returnpolicy.html")


@auth.route('/delete', methods=['GET', 'POST'])  # creates a page for deleting account
def delete_user():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')

        user = User.query.filter_by(email=email).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            flash(f"Account deleted for, {firstName.title()}", category="Success")

        else:
            flash("No existing user found!", category='Error')
            return redirect(url_for('views.home'))
    return render_template("delete.html", user=current_user)


@auth.route('/userProfile')  # routes to user Profile page; still need to test
def userProfile():
    name = "Christian Hernandez"
    vinylsSold = "241"
    followers = "841"
    return render_template("user-profile.html", name=name, vinylsSold=vinylsSold, followers=followers,
                           user=current_user)


@auth.route('/editUserProfile')  # routes to Profile editing page
def editUserProfile():
    return render_template("edit-user-profile.html", user=current_user)


@auth.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'Brand "{getbrand}" added!', 'success')
        db.session.commit()
        return redirect(url_for('a.addbrand'))

    return render_template('addbrand.html', user=current_user, brands='brands')


@auth.route('/addcategory', methods=['GET', 'POST'])
def addcategory():
    if request.method == "POST":
        getbrand = request.form.get('category')
        category = Category(name=getbrand)
        db.session.add(category)
        flash(f'Category "{getbrand}" added!', 'success')
        db.session.commit()
        return redirect(url_for('a.addbrand'))

    return render_template('addbrand.html', user=current_user)


@auth.route('/addproduct', methods=['POST', 'GET'])
def addproduct():
    brands = Brand.query.all()
    categories = Category.query.all()
    form = Addproducts(request.form)
    if request.method == "POST":
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        description = form.description.data
        brand = request.form.get('brand')
        category = request.form.get('category')
        image_1 = photos.save(request.files.get('image_1'))
        image_2 = photos.save(request.files.get('image_2'))
        image_3 = photos.save(request.files.get('image_3'))
        addpro = Addproduct(name=name, price=price, discount=discount, stock=stock, description=description,
                            brand_id=brand, category_id=category, image_1=image_1, image_2=image_2,
                            image_3=image_3)
        db.session.add(addpro)
        flash(f'Product {name} added!!', category='success')
        db.session.commit()
        return redirect(url_for('views.home'))
    return render_template('addproduct.html', title="Add Product", form=form, user=current_user,
                           brands=brands, categories=categories)


@auth.route('/adminpage')  # used to debug inventory system
def adminpage():
    products = Addproduct.query.all()
    return render_template("adminpage.html", title='Admin Page', products=products, user=current_user)


@auth.route('/genres')
def brands():
    genre = Brand.query.order_by(Brand.id.desc()).all()
    return render_template('genre.html', title="Genre page", genre=genre, user=current_user)


@auth.route('/artists')
def artists():
    artists = Category.query.order_by(Category.id.desc()).all()
    return render_template('genre.html', title="artists page", artists=artists, user=current_user)


@auth.route('/updategenres/<int:id>', methods=['GET', 'POST'])
def updategenres(id):
    updategenres = Brand.query.get(id)
    brand = request.form.get('brand')
    if request.method == "POST":
        updategenres.name = brand
        flash(f'Genre updated!', category='success')
        db.session.commit()
        return redirect(url_for('views.home'))  # reroutes to home
    return render_template('updategenres.html', title="Update Genre Page", updategenres=updategenres, user=current_user)


@auth.route('/updateartists/<int:id>', methods=['GET', 'POST'])
def updateartists(id):
    updateartists = Category.query.get(id)
    category = request.form.get('category')
    if request.method == "POST":
        updateartists.name = category
        flash(f'Artist updated!', category='success')
        db.session.commit()
        return redirect(url_for('views.home'))  # reroutes to home
    return render_template('updategenres.html', title="Update Category Page", updateartists=updateartists,
                           user=current_user)


@auth.route('/updateproduct/<int:id>', methods=['GET', 'POST'])
def updateproduct(id):
    brands = Brand.query.all()
    categories = Category.query.all()
    product = Addproduct.query.get_or_404(id)
    brand = request.form.get('brand')
    category = request.form.get('category')
    form = Addproducts(request.form)
    if request.method == "POST":
        product.name = form.name.data
        product.price = form.price.data
        product.description = form.description.data
        product.discount = form.discount.data
        product.stock = form.stock.data
        product.category_id = category
        product.brand_id = brand
        db.session.commit()
        flash(f"Product Updated!", category="success")
    form.name.data = product.name
    form.price.data = product.price
    form.description.data = product.description
    form.stock.data = product.stock
    form.discount.data = product.discount
    return render_template('updateproduct.html', form=form, user=current_user, brands=brands, categories=categories,
                           product=product)


@auth.route('/deletegenre/<int:id>', methods=['GET', 'POST'])
def deletegenre(id):
    brand = Brand.query.get_or_404(id)
    if request.method == "POST":
        db.session.delete(brand)
        flash(f"The genre {brand.name} was deleted from your database")
        db.session.commit()
        return redirect(url_for('views.home'))
    flash(f"The genre {brand.name} can't be  deleted from your database")
    return redirect(url_for('views.home'))


@auth.route('/deleteartist/<int:id>', methods=['GET', 'POST'])
def deleteartist(id):
    category = Category.query.get_or_404(id)
    if request.method == "POST":
        db.session.delete(category)
        flash(f"The artist {category.name} was deleted from your database")
        db.session.commit()
        return redirect(url_for('views.home'))
    flash(f"The artist {category.name} can't be  deleted from your database")
    return redirect(url_for('views.home'))


@auth.route('/deleteproduct/<int:id>', methods=['POST'])
def deleteproduct(id):
    product = Addproduct.query.get_or_404(id)
    if request.method == "POST":
        db.session.delete(product)
        db.session.commit()
        flash(f'The product {product.name} was delete from your record', 'success')
        return redirect(url_for('views.home'))
    flash(f'Can not delete the product', category='success')
    return redirect(url_for('views.home'))


@auth.route('/inventory')
def inventory():
    products = Addproduct.query.filter(Addproduct.stock > 0)
    brands = Brand.query.join(Addproduct, (Brand.id == Addproduct.brand_id)).all()
    categories = Category.query.join(Addproduct, (Category.id == Addproduct.category_id)).all()

    return render_template('inventory.html', user=current_user, products=products, brands=brands, categories=categories)


@auth.route('/product/<int:id>')
def single_page(id):
    product = Addproduct.query.get_or_404(id)
    return render_template('single_page.html', product=product, user=current_user)


@auth.route('/genres/<int:id>')
def get_genre(id):
    brand = Addproduct.query.filter_by(brand_id=id)
    brands = Brand.query.join(Addproduct, (Brand.id == Addproduct.brand_id)).all()
    categories = Category.query.join(Addproduct, (Category.id == Addproduct.category_id)).all()
    products = Addproduct.query.filter(Addproduct.stock > 0)
    return render_template('inventory.html', brand=brand, brands=brands, user=current_user, products=products,
                           categories=categories)


@auth.route('/artists/<int:id>')
def get_artist(id):
    category = Addproduct.query.filter_by(category_id=id)
    brands = Brand.query.join(Addproduct, (Brand.id == Addproduct.brand_id)).all()
    categories = Category.query.join(Addproduct, (Category.id == Addproduct.category_id)).all()
    products = Addproduct.query.filter(Addproduct.stock > 0)
    artists = Category.query.order_by(Category.id.desc()).all()

    return render_template('inventory.html', artists=artists, category=category, products=products,
                           categories=categories, brands=brands, user=current_user)


def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False


@auth.route('/addcart', methods=['POST', 'GET'])
def AddCart():
    try:
        product_id = request.form.get('product_id')
        quantity = request.form.get('quantity')
        product = Addproduct.query.filter_by(id=product_id).first()
        if product_id and quantity and request.method == "POST":
            DictItems = {product_id: {'name': product.name, 'price': product.price, 'discount': product.discount,
                                      'quantity': quantity, 'image': product.image_1}}
            if 'Shopcart' in session:
                print(session['Shoppingcart'])
                if product_id in session['Shoppingcart']:
                    print("Item already in cart")
            else:
                session['Shoppingcart'] = MagerDicts(session['Shoppingcart'], DictItems)
                return redirect(request.referrer)
        else:
            session['Shoppingcart'] =DictItems
            return redirect (request.referrer)
    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)


@auth.route('/carts')
def getCart():
    if 'Shoppingcart' not in session:
        flash("Cart empty!", category="warning")
        return redirect(request.referrer)
    subtotal = 0
    grandtotal = 0
    for key, product in session ['Shoppingcart'].items():
        discount = (product['discount']/100) * float(product['price'])
        subtotal += float(product['price']) * int(product['quantity'])
        subtotal -= discount
        grandtotal = subtotal
    return render_template('/carts.html', user = current_user, grandtotal = grandtotal)



@auth.route('/addwish', methods=['POST', 'GET'])
def AddWish():
    try:
        product_id = request.form.get('product_id')
        quantity = request.form.get('quantity')
        product = Addproduct.query.filter_by(id=product_id).first()
        if product_id and quantity and request.method == "POST":
            DictItems = {product_id: {'name': product.name, 'price': product.price, 'discount': product.discount,
                                      'quantity': quantity, 'image': product.image_1}}
            if 'ShopcartWish' in session:
                print(session['ShoppingcartWish'])
                if product_id in session['ShoppingcartWish']:
                    print("Item already in cart")
            else:
                session['ShoppingcartWish'] = MagerDicts(session['ShoppingcartWish'], DictItems)
                return redirect(request.referrer)
        else:
            session['ShoppingcartWish'] =DictItems
            return redirect(request.referrer)
    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)

@auth.route('/wish')
def getWish():
    return render_template('/wish.html', user = current_user)

@auth.route('/checkout')  # creates a page for checkouts
def checkout():
    return render_template("checkout.html", user=current_user)


@auth.route('/discounts')  # creates a page for discount offers
def discounts():
    return render_template("discounts.html", user=current_user)
