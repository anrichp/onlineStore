from sqlalchemy import Column, String, Integer, Date

from base import Base, engine, Session

session = Session()

class User(Base):
    __tablename__ = 'User'

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email_address = Column(String(120), unique=True, nullable=False)
    contact_number = Column(String(20), unique=True)
    type = Column(String(20))
    # init method not required as declaritive base creates that for us

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'user'
    }

    def __init__(self, first_name, last_name, email_address, contact_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.contact_number = contact_number

    @classmethod
    def createUser(cls, **kw):
        obj = cls(**kw)
        session.add(obj)
        session.commit()
        session.close()


class Seller(User):

    __mapper_args__ = {
        'polymorphic_identity': 'seller'
    }


class Customer(User):

    __mapper_args__ = {
        'polymorphic_identity': 'customer'
    }


class WarehouseStaff(User):

    __mapper_args__ = {
        'polymorphic_identity': 'warehouseStaff'
    }
