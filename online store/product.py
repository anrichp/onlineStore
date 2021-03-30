from sqlalchemy import Column, String, Integer, Date

from base import Base, engine, Session

session = Session()


class ProductCatalogue(Base):
    __tablename__ = 'productCatalogue'

    product_id = Column(Integer, primary_key=True)
    product_title = Column(String(50), nullable=False)
    product_description = Column(String(120), nullable=False)
    product_price = Column(Numeric(12,2), nullable=False)
    seller_id = Column(Integer, ForeignKey('Seller.user_id'))
    category_id = Column(Integer, ForeignKey('Category.category_id'))
    location_id = Column(Integer, ForeignKey('Location.location_id'))
    status_id = Column(Integer, ForeignKey('Status.status_id'))

