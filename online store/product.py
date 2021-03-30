from sqlalchemy import Column, String, Integer, Date

from base import Base, engine, Session

session = Session()


class Product(Base):
    __tablename__ = 'product'

    product_id = Column(Integer, primary_key=True)
    product_title = Column(String(50), nullable=False)
    product_description = Column(String(120), nullable=False)
    product_category = Column(String(50), nullable=False)
    product_price = Column(Numeric(12, 2), nullable=False)
    quantity = Column(Numeric(12), nullable=False)
    product_location = Column(String(50), nullable=False)
    product_status = Column(String(50), nullable=False)
    product_catalog_id = Column(Integer, ForeignKey("Catalog.id"))
