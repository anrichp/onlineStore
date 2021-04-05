from base import Session, engine, Base
from shopping import Order
from users import Customer

Base.metadata.create_all(engine, checkfirst=True)

quintus = Customer('Quintus', 'Potgieter', 'anrichp@gmail.com', '07907451834')
o1 = Order(quintus)

