from user import Customer
from base import Session, engine, Base

Base.metadata.create_all(engine)

session = Session()

Customer.createUser(first_name='Quintus', last_name='Potgieter', email_address='quintus@gmail.com',
                      contact_number='0736229189')

Customer.searchProduct('laptop')

for user in users:
    print(user.first_name, user.last_name, user.type)
