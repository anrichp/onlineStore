from user import Customer, User
from shopping import Order
from base import Session, engine, Base
from sqlalchemy.orm import relationship

Base.metadata.create_all(engine)

session = Session()

quintus = Customer(first_name='Quintus', last_name='Potgieter', email_address='quintus@gmail.com',
                      contact_number='0736229189')

quintus.searchProduct('laptop')

for user in users:
    print(user.first_name, user.last_name, user.type)
