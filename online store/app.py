from base import Session, engine, Base
from users import Customer
from shopping import Order

Base.metadata.create_all(engine, checkfirst=True)

