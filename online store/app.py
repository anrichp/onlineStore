from user import User
from base import Session, engine, Base

Base.metadata.create_all(engine)

session = Session()

User.createUser(first_name='Quintus', last_name='Potgieter',email_address='quintus@gmail.com', contact_number='0736229189')

users = session.query(User).all()

for user in users:
    print(user.first_name)