from base import Session, engine, Base
from shopping import Order
from users import Customer


session = Session()

Base.metadata.create_all(engine, checkfirst=True)

quintus = Customer('Anrich', 'Quintus', 'anrichp@gmail.com', '07907451834')

session.add(quintus)

session.commit()