from users import User, Customer
from shopping import Order
from base import Session, engine, Base

session = Session()

quintus = Customer(first_name='Quintus', last_name='Potgieter', email_address='quintus@gmail.com',
                   contact_number='0736229189')
