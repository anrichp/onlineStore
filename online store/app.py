from user import Orginisation
from base import Session, engine, Base

Base.metadata.create_all(engine)

session = Session()

Orginisation.createUser(first_name='Quintus', last_name='Potgieter', email_address='quintus@gmail.com',
                        contact_number='0736229189', company_name='test company', tax_certificate='1234')

users = session.query(Orginisation).all()

for user in users:
    print(user.first_name, user.last_name, user.company_name)
