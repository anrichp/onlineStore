from sqlalchemy import Column, String, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from base import Base, engine, Session


class Product(Base):
    __tablename__ = 'product'

    product_id = Column(Integer, primary_key=True)
    product_title = Column(String(50), nullable=False)
    product_description = Column(String(120), nullable=False)
    product_price = Column(Numeric(12, 2), nullable=False)
    product_quanity = Column(Integer, ForeignKey('quantity.quantity_id'))
    product_location = Column(Integer, ForeignKey('location.location_id'))
    product_status = Column(Integer, ForeignKey(('productStatus.status_id')))


class ProductCatalogue(Base):
    __tablename__ = 'productCatalogue'

    catalogue_id = Column(Integer, primary_key=True)
    seller_id = Column(Integer, ForeignKey('user.user_id'))
    products = relationship('Product', backref='product')


class Category(Base):
    __tablename__ = 'category'

    category_id = Column(Integer, primary_key=True)
    category_name = Column(String(50), nullable=False)


class Location(Base):
    __tablename__ = 'location'

    location_id = Column(Integer, primary_key=True)
    product_location = Column(String(50), nullable=False)


class Quantity(Base):
    __tablename__ = 'quantity'

    quantity_id = Column(Integer, primary_key=True)
    quantity = Column(Numeric(20), nullable=False)


class ProductStatus(Base):
    __tablename__ = 'productStatus'

    status_id = Column(Integer, primary_key=True)
    product_status = Column(String(50), nullable=False)
