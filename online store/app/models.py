from datetime import datetime
from flask import current_app, request, url_for
from . import db

# User Models
class User(db.Model):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email_address = Column(String(120), unique=True, nullable=False)
    contact_number = Column(String(20), unique=True)
    type = Column(String(20))

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
    shipping_address = Column(String(50))
    billing_address = Column(String(50))
    payment_details = Column(String(50))
    orders = relationship('Order', backref='user')

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
    job_title = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'warehouseStaff'
    }


class Seller(User):
    store_name = Column(String(50))

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
    proof_of_identity = Column(String(50))
    proof_of_banking = Column(String(50))

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
    company_name = Column(String(50))
    tax_certificate = Column(String(50))

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
association_table = Table('product_catalogue', Base.metadata, Column('productCatalogue_id', Integer, ForeignKey(
    'productCatalogue.catalogue_id')), Column('product_id', Integer, ForeignKey('product.product_id')))


class Product(db.Model):
    __tablename__ = 'product'

    product_id = Column(Integer, primary_key=True)
    product_title = Column(String(50), nullable=False)
    product_description = Column(String(120), nullable=False)
    product_price = Column(Numeric(12, 2), nullable=False)
    category_category_id = Column(Integer, ForeignKey('category.category_id'))
    location_location_id = Column(Integer, ForeignKey('location.location_id'))
    quantity_quantity_id = Column(Integer, ForeignKey('quantity.quantity_id'))
    productstatus_status_id = Column(
        Integer, ForeignKey('productStatus.status_id'))
    productcatalogue_catalogue_id = Column(
        Integer, ForeignKey('productCatalogue.catalogue_id'))

    # Relationships
    category = relationship('category', foreign_keys=category_category_id)
    location = relationship('location', foreign_keys=location_location_id)
    quantity = relationship('quantity', foreign_keys=quantity_quantity_id)
    productstatus = relationship(
        'productStatus', foreign_keys=productstatus_status_id)
    productcatalogue = relationship(
        'productCatalogue', foreign_keys=productcatalogue_catalogue_id)

class Category(db.Model):
    __tablename__ = 'category'

    category_id = Column(Integer, primary_key=True)
    category_name = Column(String(50), nullable=False)


class Location(db.Model):
    __tablename__ = 'location'

    location_id = Column(Integer, primary_key=True)
    product_location = Column(String(50), nullable=False)


class Quantity(db.Model):
    __tablename__ = 'quantity'

    quantity_id = Column(Integer, primary_key=True)
    quantity = Column(Numeric(20), nullable=False)


class ProductStatus(db.Model):
    __tablename__ = 'productStatus'

    status_id = Column(Integer, primary_key=True)
    product_status = Column(String(50), nullable=False)

# Product Catalogue Model
class ProductCatalogue(db.Model):
    __tablename__ = 'productCatalogue'

    catalogue_id = Column(Integer, primary_key=True)
    seller_id = Column(Integer, ForeignKey('user.user_id'))

    # Relationships
    user = relationship('User', backref='productCatalogue',
                        foreign_keys=seller_id)
    products = relationship('Product', secondary=association_table)

    @ classmethod
    def createProduct(cls, **kw):
        obj = cls(**kw)
        session.add(obj)
        session.commit()
        session.close()

# Shopping Basket Model
class ShoppingBasket(db.Model):
    __tablename__ = 'shoppingBasket'

    basket_id = Column(Integer, primary_key=True)
    customer_user_id = Column(Integer, ForeignKey('user.user_id'))
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    quantity = Column(Numeric(10))
    total_cost = Column(Numeric(12, 2), nullable=False)

    # Relationships
    user = relationship('User', backref='shoppingBasket', foreign_keys=customer_user_id)
    products = relationship('Product', backref='shoppingBasket')

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

    order_id = Column(Integer, primary_key=True)
    date_placed = Column(DateTime, default=datetime.datetime.utcnow)
    # total = Column(Numeric(12, 2), nullable=False)
    order_status = Column(String(10), nullable=False)
    customer_id = Column(Integer, ForeignKey('user.user_id'))