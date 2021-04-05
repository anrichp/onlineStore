import datetime
from sqlalchemy import Column, String, Integer, Date
from base import Base, engine, Session

session = Session()


class ShoppingBasket(Base):
    __tablename__ = 'ShoppingBasket'

    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    def checkout(self, products):
        pass

    def update(self, products):
        pass

    def delete(self, products):
        pass
