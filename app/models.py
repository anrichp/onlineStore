from datetime import datetime
import sqlalchemy.types as types
from flask import current_app, request, url_for
from . import db

"""Declaring Models

    Using the SQLAlchemy Library the online store models are defined below.
    Each class in the models.py file with exeption to the inherited classes 
    represent a table in the database.

    Example Table Declaration

    class User(db.Model):
        __tablename__ = 'User'

        id = db.Column(db.Integer, primary_key=True)
        sername = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)

        # Relationship
        addresses = db.relationship('Address', backref='person', lazy=True)

    Typically a table declaration contains:
     - Table name
     - Variables representing columns
     - relaionships

"""

class User(db.Model):
    """User Table

        The user table is responsble for storing all users in the online store.
        The type column is used to indicate the user type. Subsequent classes/tables that inherit user 
        have a mapping arg which ensures that the type is updated according to the class or table used.

    """
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email_address = db.Column(db.String(120), unique=True, nullable=False)
    contact_number = db.Column(db.String(20), unique=True)
    type = db.Column(db.String(20))

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'user'
    }


class Customer(User):
    """Customer Table

        The customer table is an example of inheritance and has a polymophic identity which ensures
        that the type field is updated according to the table or class used.

    """
    shipping_address = db.Column(db.String(50))
    billing_address = db.Column(db.String(50))
    payment_details = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'customer'
    }


class WarehouseStaff(User):
    job_title = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'warehouseStaff'
    }


class Seller(User):
    store_name = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'seller'
    }


class SiteOwner(Seller):

    __mapper_args__ = {
        'polymorphic_identity': 'siteOwner'
    }


class ThirdPartySeller(Seller):

    __mapper_args__ = {
        'polymorphic_identity': 'thirdPartySeller'
    }


class Individual(ThirdPartySeller):
    proof_of_identity = db.Column(db.String(50))
    proof_of_banking = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'individual'
    }


class Orginisation(ThirdPartySeller):
    company_name = db.Column(db.String(50))
    tax_certificate = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'orginisation'
    }


#  Product association table
association_table = db.Table('product_catalogue', db.metadata, db.Column('productCatalogue_id', db.Integer, db.ForeignKey(
    'productCatalogue.catalogue_id')), db.Column('product_id', db.Integer, db.ForeignKey('product.product_id')))


class Product(db.Model):

    __tablename__ = 'product'

    product_id = db.Column(db.Integer, primary_key=True)
    product_title = db.Column(db.String(50), nullable=False)
    product_description = db.Column(db.String(120), nullable=False)
    product_price = db.Column(db.Numeric(12, 2), nullable=False)
    product_quantity = db.Column(db.Numeric(12, 0), nullable=False)
    category_category_id = db.Column(
        db.Integer, db.ForeignKey('category.category_id'))
    location_location_id = db.Column(
        db.Integer, db.ForeignKey('location.location_id'))
    productstatus_status_id = db.Column(
        db.Integer, db.ForeignKey('productStatus.status_id'))
    productcatalogue_catalogue_id = db.Column(
        db.Integer, db.ForeignKey('productCatalogue.catalogue_id'))

    # Relationships
    category = db.relationship('Category', foreign_keys=category_category_id)
    location = db.relationship('Location', foreign_keys=location_location_id)
    productstatus = db.relationship(
        'ProductStatus', foreign_keys=productstatus_status_id)
    productcatalogue = db.relationship(
        'ProductCatalogue', foreign_keys=productcatalogue_catalogue_id)


class Category(db.Model):
    __tablename__ = 'category'

    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50), nullable=False)


class Location(db.Model):
    __tablename__ = 'location'

    location_id = db.Column(db.Integer, primary_key=True)
    product_location = db.Column(db.String(50), nullable=False)


class ProductStatus(db.Model):
    __tablename__ = 'productStatus'

    status_id = db.Column(db.Integer, primary_key=True)
    product_status = db.Column(db.String(50), nullable=False)


class ProductCatalogue(db.Model):
    __tablename__ = 'productCatalogue'

    catalogue_id = db.Column(db.Integer, primary_key=True)
    seller_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    # Relationships
    user = db.relationship('User', backref='productCatalogue',
                           foreign_keys=seller_id)
    products = db.relationship('Product', secondary=association_table)


class Order(db.Model):
    __tablename__ = 'order'

    order_id = db.Column(db.Integer, primary_key=True)
    customer_user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    total = db.Column(db.Numeric(12, 2), nullable=False)
    order_status_id = db.Column(
        db.Integer, db.ForeignKey('orderStatus.status_id'))

    # Relationship
    line_items = db.relationship("OrderLine", backref='order')


class OrderLine(db.Model):
    __tablename__ = 'orderLines'

    orderlines_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
    quantity = db.Column(db.Numeric(10, 0))
    
    # Relationship
    product = db.relationship("Product")


class Orderstatus(db.Model):
    __tablename__ = 'orderStatus'
    status_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), nullable=False)


class Payment(db.Model):
    __tablename__ = 'payment'
    payment_id = db.Column(db.Integer, primary_key=True)
    order_order_id = db.Column(
        db.Integer, db.ForeignKey('order.order_id'))
    paymentmethod_method_id = db.Column(
        db.Integer, db.ForeignKey('paymentMethod.method_id'))
    status = db.Column(db.String(20), nullable=False)
    total = db.Column(db.Numeric(12, 2))

    # Relationships
    order = db.relationship('Order', foreign_keys=order_order_id)
    paymentmethod = db.relationship(
        'Paymentmethod', foreign_keys=paymentmethod_method_id)


class Paymentmethod(db.Model):
    __tablename__ = 'paymentMethod'
    method_id = db.Column(db.Integer, primary_key=True)
    payment_type = db.Column(db.String(20), nullable=False)
