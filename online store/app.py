from base import Session, engine, Base
from product import Product, ProductCatalogue
from users import *
from shopping import Order


session = Session()

Base.metadata.create_all(engine, checkfirst=True)

anrich = Seller('Anrich', 'Potgieter', 'anrichp@gmail.com', '07907451834')
