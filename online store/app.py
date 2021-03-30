from user import Individual
from base import Session, engine, Base

Base.metadata.create_all(engine)

session = Session()

Individual.createUser(first_name='Quintus', last_name='Potgieter', email_address='quintus@gmail.com',
                      contact_number='0736229189', proof_of_identity='identity', proof_of_banking='banking')

users = session.query(Individual).all()

for user in users:
    print(user.first_name, user.last_name, user.type)
