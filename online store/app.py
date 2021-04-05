from base import Session, engine, Base
from users import Customer
from shopping import Order

quintus = Customer('Quintus', 'Potgieter', 'anrichp@gmail.com', '07907451834')
o1 = Order(quintus)

