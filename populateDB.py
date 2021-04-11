from app import db
from app.models import User, Orginisation, Product, Category, Location, Quantity, ProductStatus, ProductCatalogue

sellerOrginisation = Orginisation(
    'Anrich', 'Potgieter', 'anrichp@gmail.com', '07907451834', 'Mordecai', '12345678')

mordecaiCatalogue = ProductCatalogue(user=sellerOrginisation)

desktop = Category(category_name='Desktop')
laptop = Category(category_name='Laptop')

warehouse = Location(product_location='Warehouse')
awaitingDelivery = Location(product_location='Awaiting Delivery')

inStock = ProductStatus(product_status='In Stock')
outStock = ProductStatus(product_status='Out Of Stock')

db.session.add(sellerOrginisation)
db.session.add(mordecaiCatalogue)
db.session.add(desktop)
db.session.add(laptop)
db.session.add(warehouse)
db.session.add(awaitingDelivery)
db.session.add(inStock)
db.session.add(outStock)

db.session.commit()

print("Added all items to the database")