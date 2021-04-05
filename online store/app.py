from base import Session, engine, Base
from shopping import Order
from users import Customer


session = Session()

Base.metadata.create_all(engine, checkfirst=True)

Anrich = Customer('Anrich', 'Potgieter', 'anrichp@gmail.com', '07907451834')
o1 = Order(user = Anrich, order_status= 'processing')

session.add(o1)

session.commit()
