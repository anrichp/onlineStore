from sqlalchemy import Column, String, Integer, Date

from base import Base, engine, Session

session = Session()


class ProductCatalogue(Base):
    __tablename__ = 'ProductCatalogue'

    product_id = Column(Integer, primary_key=True)
    product_title = Column(String(50), nullable=False)
    product_description = Column(String(120), nullable=False)
    product_price = Column(Numeric(12, 2), nullable=False)
    quantity_id = Column(Integer, ForeignKey('Quantity.quintity_id'))
    category_id = Column(Integer, ForeignKey('Category.category_id'))
    location_id = Column(Integer, ForeignKey('Location.location_id'))
    status_id = Column(Integer, ForeignKey('Status.status_id'))
    seller_id = Column(Integer, ForeignKey('Seller.user_id'))


class Category(Base):
    __tablename__ = 'Category'

    category_id = Column(Integer, primary_key=True)
    category_name = Column(String(50), nullable=False)


class Location(Base):
    __tablename__ = 'Location'

    location_id = Column(Integer, primary_key=True)
    product_location = Column(String(50), nullable=False)


class Quantity(Base):
    __tablename__ = 'Quantity'

    quantity_id = Column(Integer, primary_key=True)
    quantity = Column(Integer(20), nullable=False)
