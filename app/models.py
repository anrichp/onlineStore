from datetime import datetime
from flask import current_app, request, url_for
from . import db

# User Models


class User(db.Model):
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

    def __init__(self, first_name, last_name, email_address, contact_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.contact_number = contact_number

    @classmethod
    def createUser(cls, **kw):
        obj = cls(**kw)
        session.add(obj)
        session.commit()
        session.close()


class Customer(User):
    shipping_address = db.Column(db.String(50))
    billing_address = db.Column(db.String(50))
    payment_details = db.Column(db.String(50))
    orders = db.relationship('Order', backref='user')

    def addToShoppingBasket(product):
        basket_item = ShoppingBasket(product=product)
        db.session.add(basket_item)
        db.session.commit()

    def searchProduct(search):
        products = Product.query.filter_by(product_title=search).all()

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

    @classmethod
    def createCatalogue(cls, **kw):
        obj = cls(**kw)
        session.add(obj)
        session.commit()
        session.close()

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

    def __init__(self, first_name, last_name, email_address, contact_number, proof_of_identity, proof_of_banking):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.contact_number = contact_number
        self.proof_of_identity = proof_of_identity
        self.proof_of_banking = proof_of_banking

    __mapper_args__ = {
        'polymorphic_identity': 'individual'
    }


class Orginisation(ThirdPartySeller):
    company_name = db.Column(db.String(50))
    tax_certificate = db.Column(db.String(50))

    def __init__(self, first_name, last_name, email_address, contact_number, company_name, tax_certificate):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.contact_number = contact_number
        self.company_name = company_name
        self.tax_certificate = tax_certificate

    __mapper_args__ = {
        'polymorphic_identity': 'orginisation'
    }


#  Product Model
association_table = db.Table('product_catalogue', db.metadata, db.Column('productCatalogue_id', db.Integer, db.ForeignKey(
    'productCatalogue.catalogue_id')), db.Column('product_id', db.Integer, db.ForeignKey('product.product_id')))


class Product(db.Model):
    __tablename__ = 'product'

    product_id = db.Column(db.Integer, primary_key=True)
    product_title = db.Column(db.String(50), nullable=False)
    product_description = db.Column(db.String(120), nullable=False)
    product_price = db.Column(db.Numeric(12, 2), nullable=False)
    category_category_id = db.Column(
        db.Integer, db.ForeignKey('category.category_id'))
    location_location_id = db.Column(
        db.Integer, db.ForeignKey('location.location_id'))
    quantity_quantity_id = db.Column(
        db.Integer, db.ForeignKey('quantity.quantity_id'))
    productstatus_status_id = db.Column(
        db.Integer, db.ForeignKey('productStatus.status_id'))
    productcatalogue_catalogue_id = db.Column(
        db.Integer, db.ForeignKey('productCatalogue.catalogue_id'))

    # Relationships
    category = db.relationship('category', foreign_keys=category_category_id)
    location = db.relationship('location', foreign_keys=location_location_id)
    quantity = db.relationship('quantity', foreign_keys=quantity_quantity_id)
    productstatus = db.relationship(
        'productStatus', foreign_keys=productstatus_status_id)
    productcatalogue = db.relationship(
        'productCatalogue', foreign_keys=productcatalogue_catalogue_id)


class Category(db.Model):
    __tablename__ = 'category'

    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50), nullable=False)


class Location(db.Model):
    __tablename__ = 'location'

    location_id = db.Column(db.Integer, primary_key=True)
    product_location = db.Column(db.String(50), nullable=False)


class Quantity(db.Model):
    __tablename__ = 'quantity'

    quantity_id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Numeric(12,0), nullable=False)


class ProductStatus(db.Model):
    __tablename__ = 'productStatus'

    status_id = db.Column(db.Integer, primary_key=True)
    product_status = db.Column(db.String(50), nullable=False)

# Product Catalogue Model


class ProductCatalogue(db.Model):
    __tablename__ = 'productCatalogue'

    catalogue_id = db.Column(db.Integer, primary_key=True)
    seller_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    # Relationships
    user = db.relationship('User', backref='productCatalogue',
                           foreign_keys=seller_id)
    products = db.relationship('Product', secondary=association_table)

    @ classmethod
    def createProduct(cls, **kw):
        obj = cls(**kw)
        session.add(obj)
        session.commit()
        session.close()

# Shopping Basket Model


class ShoppingBasket(db.Model):
    __tablename__ = 'shoppingBasket'

    basket_id = db.Column(db.Integer, primary_key=True)
    customer_user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    quantity = db.Column(db.Numeric(10))
    product_product_id = db.Column(
        db.Integer, db.ForeignKey('Product.product_id'))
    total_cost = db.Column(db.Numeric(12, 2), nullable=False)

    # Relationships
    user = db.relationship('User', backref='shoppingBasket',
                           foreign_keys=customer_user_id)
    products = db.relationship(
        'Product', backref='shoppingBasket', foreign_keys=product_product_id)

    def checkout(self, products):
        pass

    def update(self, products):
        pass

    def delete(shopping_basket):
        session.delete(shopping_basket)
        session.commit()

# Order Model


class Order(db.Model):
    __tablename__ = 'order'

    order_id = db.Column(db.Integer, primary_key=True)
    shopping_basket_id = db.Column(
        db.Integer, db.ForeignKey('shoppingBasket.basket_id'))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    total = db.Column(db.Numeric(12, 2), nullable=False)
    order_status_id = db.Column(
        db.Integer, db.ForeignKey('orderStatus.status_id'))


class Orderstatus(db.Model):
    __tablename__ = 'orderStatus'
    status_id = db.Column(db.Integer, primary_key=True)
    status = Column(db.String(20), nullable=False)

# Payment Model


class Payment(db.Model):
    __tablename__ = 'paymentMethod'
    payment_id = db.Column(db.Integer, primary_key=True)
    order_order_id = db.Column(
        db.Integer, db.ForeignKey('paymentMethod.method_id'))
    paymentmethod_method_id = db.Column(
        db.Integer, db.ForeignKey('paymentMethod.method_id'))
    status = db.Column(db.String(20), nullable=False)
    total = db.Column(db.Numeric(12, 2))

    # Relationships
    order = db.relationship('Order', foreign_keys=order_order_id)
    paymentmethod = db.relationship('Paymentmethod', foreign_keys=paymentmethod_method_id)

class Paymentmethod(db.Model):
    __tablename__='paymentMethod'
    method_id = db.Column(db.Integer, primary_key=True)
    payment_type = db.Column(db.String(20), nullable=False)