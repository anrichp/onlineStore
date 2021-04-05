from base import Session, engine, Base
from shopping import Order
from users import Customer

Base.metadata.create_all(engine, checkfirst=True)

