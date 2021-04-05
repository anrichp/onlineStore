from base import Session, engine, Base
from users import Customer
from shopping import Order

session = Session()

Base.metadata.create_all(engine, checkfirst=True)

quintus = Customer('Anrich', 'Quintus', 'anrichp@gmail.com', '07907451834')

session.add(quintus)

session.commit()