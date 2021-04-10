import datetime
from sqlalchemy import Column, String, Integer, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from base import Base, engine, Session


class ShoppingBasket(Base):
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


class Order(Base):
    __tablename__ = 'order'

    order_id = Column(Integer, primary_key=True)
    date_placed = Column(DateTime, default=datetime.datetime.utcnow)
    # total = Column(Numeric(12, 2), nullable=False)
    order_status = Column(String(10), nullable=False)
    customer_id = Column(Integer, ForeignKey('user.user_id'))
