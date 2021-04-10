from flask import render_template, redirect, url_for, session
from flask import request
from . import main
from .. import db
from ..models import User, Product, ProductCatalogue, ShoppingBasket, Order

@main.route('/')
def index():
    return render_template('index.html')
