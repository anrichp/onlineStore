from app import db
from app.models import User, Orginisation, Product, Category, Location, ProductStatus, ProductCatalogue

sellerOrginisation = Orginisation(
    'Anrich', 'Potgieter', 'anrichp@gmail.com', '07907451834', 'Mordecai', '12345678')

mordecaiCatalogue = ProductCatalogue(user=sellerOrginisation)

desktop = Category(category_name='Desktop')
laptop = Category(category_name='Laptop')

warehouse = Location(product_location='Warehouse')
awaitingDelivery = Location(product_location='Awaiting Delivery')

inStock = ProductStatus(product_status='In Stock')
outStock = ProductStatus(product_status='Out Of Stock')

in_progress = Orderstatus(status='In Progress')
processing = Orderstatus(status='Processing')
pending_payment = Orderstatus(status='Pending Payment')
awaiting_picking = Orderstatus(status='Awaiting Picking')
ready_for_delivery = Orderstatus(status='Ready For Delivery')
shipped = Orderstatus(status='Shipped')


db.session.add(sellerOrginisation)
db.session.add(mordecaiCatalogue)
db.session.add(desktop)
db.session.add(laptop)
db.session.add(warehouse)
db.session.add(awaitingDelivery)
db.session.add(inStock)
db.session.add(outStock)
db.session.add_all([in_progress, processing, pending_payment,
                   awaiting_picking, ready_for_delivery, shipped])

db.session.commit()

print("Added all items to the database")
