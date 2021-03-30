from user import Seller
from base import Session, engine, Base

Base.metadata.create_all(engine)

session = Session()

Seller.createUser(first_name='Quintus', last_name='Potgieter',email_address='quintus@gmail.com', contact_number='0736229189')

users = session.query(Seller).all()

for user in users:
    print(user.first_name, user.last_name)