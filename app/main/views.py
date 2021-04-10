from flask import render_template, redirect, url_for, jsonify, session
from flask import request
from . import main
from .forms import NewProduct
from .. import db
from ..models import User, Product


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/newproduct', methods=['GET', 'POST'])
def newProduct():
    form = NewProduct()

    product = Product(product_title=form.product_name.data, product_description=form.product_description.data, product_price=form.product_price.data, category_category_id=form.category.data,
                      location_location_id=form.locaton.data, quantity_quantity_id=form.quantity.data, productstatus_status_id=form.status.data, productcatalogue_catalogue_id=form.product_catalogue)

    db.session.add(product)
    db.commit()

    return render_template('newProduct.html', form=form)