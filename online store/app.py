from base import Session, engine, Base
from catalogue import *
from users import *
from shopping import *


session = Session()

Base.metadata.create_all(engine, checkfirst=True)

anrich = Seller('Anrich', 'Potgieter', 'anrichp@gmail.com', '07907451834')

product1 = Product(product_title='Laptop',
                   product_description='Description', product_price=25)

product2 = Product(product_title='Not Laptop',
                   product_description='Description', product_price=25)

anrich_catalogue = ProductCatalogue()

anrich_catalogue.user = anrich

anrich_catalogue.products = [product2]

session.add(anrich_catalogue)

session.commit()
