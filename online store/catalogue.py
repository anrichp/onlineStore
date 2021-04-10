from sqlalchemy import Column, String, Integer, Numeric, ForeignKey, Table
from sqlalchemy.orm import relationship
from base import Base, engine, Session


association_table = Table('product_catalogue', Base.metadata, Column('productCatalogue_id', Integer, ForeignKey(
    'productCatalogue.catalogue_id')), Column('product_id', Integer, ForeignKey('product.product_id')))


class Product(Base):
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


class ProductCatalogue(Base):
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