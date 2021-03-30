from sqlalchemy import Column, String, Integer, Date

from base import Base, engine, Session

session = Session()


class ProductCatalogue(Base):
    __tablename__ = 'productCatalogue'

    product_catalog_id = Column(Integer, primary_key=True)
    seller_id = Column(Integer, ForeignKey('User.id'))
