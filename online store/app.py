from user import Seller
from base import Session, engine, Base

Base.metadata.create_all(engine)

session = Session()

Anrich = Seller(first_name='Anrich',
              last_name='Potgieter',
              email_address='anrichp@gmail.com',
              contact_number='07907451834',)

session.add(Anrich)
session.commit()
session.close()

users = session.query(Seller).all()

for user in users:
    print(user.type)
