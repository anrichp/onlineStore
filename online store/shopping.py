import datetime
from sqlalchemy import Column, String, Integer, DateTime
from base import Base, engine, Session

session = Session()


class ShoppingBasket(Base):
    __tablename__ = 'ShoppingBasket'

    basket_id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    def checkout(self, products):
        pass

    def update(self, products):
        pass

    def delete(self, products):
        pass


class Order(Base):
    __tablename__ = 'Order'

    order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('users.User.user_id'))
    date_placed = Column(DateTime, default=datetime.datetime.utcnow)
    total = Column(Numeric(12, 2), nullable=False)
    order_status = Column(String(10), nullable=False)

Base.metadata.create_all(engine)