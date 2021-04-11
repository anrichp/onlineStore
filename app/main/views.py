from flask import render_template, redirect, url_for, jsonify, session
from flask import request
from . import main
from .forms import NewProduct, NewCategory
from .. import db
from ..models import *


@main.route('/')
def index():
    products = db.session.query(Product).all()
    categories = db.session.query(Category).all()
    return render_template('index.html', products=products, categories=categories)


@main.route('/newcategory', methods=['GET', 'POST'])
def newCategory():
    form = NewCategory()

    if request.method == 'POST' and form.validate_on_submit():
        category = Category(category_name=form.category_name.data)

        db.session.add(category)
        db.session.commit()

        return redirect(url_for('.index'))

    return render_template('newCategory.html', form=form)


@main.route('/newproduct', methods=['GET', 'POST'])
def newProduct():
    form = NewProduct()

    if request.method == 'POST' and form.validate_on_submit():

        product = Product(product_title=form.product_name.data, product_description=form.product_description.data, product_price=form.product_price.data, product_quantity=form.quantity.data, category=form.category.data,
                          location=form.location.data, productstatus=form.status.data, productcatalogue=form.product_catalogue.data)

        db.session.add(product)
        db.session.commit()

        return redirect(url_for('.index'))

    return render_template('newProduct.html', form=form)


@main.route('/product/<int:id>')
def productDetails(id):
    product = db.session.query(Product).get(id)

    return render_template('product.html', product=product)
