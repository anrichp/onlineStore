from flask import render_template, redirect, url_for, jsonify, session, flash
from flask import request
from . import main
from .forms import NewProduct, NewCategory
from .. import db
from ..models import *
from decimal import *


@main.route('/')
def index():
    """Root Decorator and Index Function

    Args:
        none.

    Returns:
        index.html with all items in the product table.

    """
    products = db.session.query(Product).all()
    categories = db.session.query(Category).all()
    return render_template('index.html', products=products, categories=categories)


@main.route('/newcategory', methods=['GET', 'POST'])
def newCategory():
    """New Category Decorator and function to append category to database

    Args:
        none.

    Returns: 
        newCategory.html with a form to append a new category to the category table.

    """
    form = NewCategory()

    if request.method == 'POST' and form.validate_on_submit():
        category = Category(category_name=form.category_name.data)

        db.session.add(category)
        db.session.commit()

        return redirect(url_for('.index'))

    return render_template('newCategory.html', form=form)


@main.route('/newproduct', methods=['GET', 'POST'])
def newProduct():
    """New Product Decorator and function to append new product to the database

    Args:
        none.

    Returns:
        ON GET:
            newProduct.html with form to append a new product to the database.

        ON POST:
            Stores a new product in the poduct table and user is redirected to index page.

    TODO:
        - Use login session to determine the seller and append the new product to the sellers catalogue.
        - Add catalogue name to catalogue model in models.py

    """
    form = NewProduct()

    if request.method == 'POST' and form.validate_on_submit():

        product = Product(product_title=form.product_name.data, product_description=form.product_description.data, product_price=form.product_price.data, product_quantity=form.quantity.data, category=form.category.data,
                          location=form.location.data, productstatus=form.status.data, productcatalogue=form.product_catalogue.data)

        db.session.add(product)
        db.session.commit()

        return redirect(url_for('.index'))

    return render_template('newProduct.html', form=form)


@main.route('/product/<int:product_id>')
def productDetails(product_id):
    """Product Details Decorator and function to display product details

    Args:
        product_id(int): Recieves product id and passes id to query.

    Returns:
        product.html which displays the details of a product.

    """
    product = db.session.query(Product).get(product_id)

    return render_template('product.html', product=product)


@main.route('/add_to_shopping_basket/<int:product_id>')
def addToBasket(product_id):
    """Add to Shopping Decorator and function to add product to in memory session

    Args:
        product_id(int): Receives product id and passes the in memory session.

    Return:
        Redirects to index when user add's item to cart.

    """
    # Determine whether basket is in session and create list in session
    if 'basket' not in session:
        session['basket'] = []

    # Append product id to session list and inform session that is has been modified
    session['basket'].append(product_id)
    session.modified = True

    return redirect(url_for('.index'))


@main.route('/shopping_basket')
def shoppingBasket():
    """Shopping Basket Decorator and function to display all items in shopping basket

    Args:
        none.

    Returns:
        shoppingBasket.html with a queried list of products in session

    """

    products = list()
    total_cost = Decimal()

    if 'basket' not in session:
        return redirect(url_for('.index'))

    # Iterate through the list of product id's and query database with product id
    for product in session['basket']:
        products.append(db.session.query(Product).get(product))

    # Iterate over products and store total price for all products in cart
    for price in products:
        total_cost += price.product_price

    return render_template('shoppingBasket.html', products=products, total=total_cost)


@main.route('/checkout')
def checkout():
    """ Checkout Decorator and function to append product/s to order

    Args:
        none.

    Returns:
        TODO: 
            - Determine which customer is creating the order
            - Redirect to the order that was created.
    """
    products = list()
    total_cost = Decimal()

    if 'basket' not in session:
        return redirect(url_for('.index'))

    for product in session['basket']:
        products.append(db.session.query(Product).get(product))

    for price in products:
        total_cost += price.product_price


@main.route('/orders')
def orders():
    """ Orders Decorator and function to view all orders

    Args:
        none.

    Returns:
        TODO:
         - Create order.html 

    """
    orders = db.query(Order).all()
    if order is None:
        return redirect(url_for('.index'))

    return render_template('orders.html', orders=orders)
