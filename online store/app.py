from user import User
from base import Session, engine, Base

Base.metadata.create_all(engine)

session = Session()

Anrich = User(first_name='Anrich',
              last_name='Potgieter',
              email_address='anrichp@gmail.com',
              contact_number='07907451834')

session.add(Anrich)
session.commit()
session.close()

users = session.query(User).all()

for user in users:
    print(user.type)
