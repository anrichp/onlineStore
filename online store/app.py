from base import Session, engine, Base
from product import *
from users import *
from shopping import *


session = Session()

Base.metadata.create_all(engine, checkfirst=True)

anrich = Seller('Anrich', 'Potgieter', 'anrichp@gmail.com', '07907451834')
product1 = Product('Laptop', 'Description', '25')

anrich_catalogue = ProductCatalogue()
anrich_catalogue.user = anrich
anrich_catalogue.products = product1
session.add(anrich_catalogue)
session.commit()