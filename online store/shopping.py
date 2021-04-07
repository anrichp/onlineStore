import datetime
from sqlalchemy import Column, String, Integer, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from base import Base, engine, Session


class ShoppingBasket(Base):
    __tablename__ = 'shoppingBasket'

    basket_id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    total_cost = Column(Numeric(12,2), nullable=False)

    #Relationship
    products = relationship('Product', backref='shoppingBasket')

    def checkout(self, products):
        pass

    def update(self, products):
        pass

    def delete(self, products):
        pass


class Order(Base):
    __tablename__ = 'order'

    order_id = Column(Integer, primary_key=True)
    date_placed = Column(DateTime, default=datetime.datetime.utcnow)
    # total = Column(Numeric(12, 2), nullable=False)
    order_status = Column(String(10), nullable=False)
    customer_id = Column(Integer, ForeignKey('user.user_id'))
