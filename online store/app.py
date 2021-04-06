from base import Session, engine, Base
from product import Product, ProductCatalogue


session = Session()

Base.metadata.create_all(engine, checkfirst=True)



session.add()

session.commit()
