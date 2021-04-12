from app import db
from app.models import User, Customer, Orginisation, Product, Category, Location, ProductStatus, ProductCatalogue, Order, OrderLine, Orderstatus

# Create seller
sellerOrginisation = Orginisation(
    'Anrich', 'Potgieter', 'anrichp@gmail.com', '07907451834', 'Mordecai', '12345678')

# Create Customer
Quintus = Customer(first_name='Quintus', last_name='Potgieter',
                   email_address='quintus123@gmail.com', contact_number='123456789')

# Create catalogue for seller
mordecaiCatalogue = ProductCatalogue(user=sellerOrginisation)

# Create categories
desktop = Category(category_name='Desktop')
laptop = Category(category_name='Laptop')

# Create product locations
warehouse = Location(product_location='Warehouse')
awaitingDelivery = Location(product_location='Awaiting Delivery')

# Create product statuses
inStock = ProductStatus(product_status='In Stock')
outStock = ProductStatus(product_status='Out Of Stock')

# Create order statuses
in_progress = Orderstatus(status='In Progress')
processing = Orderstatus(status='Processing')
pending_payment = Orderstatus(status='Pending Payment')
awaiting_picking = Orderstatus(status='Awaiting Picking')
ready_for_delivery = Orderstatus(status='Ready For Delivery')
shipped = Orderstatus(status='Shipped')


# Create prouducs
p1 = Product(
    product_title='HP Pavilion x360 14" 2 in 1 Laptop - Intel® Core™ i7, 512 GB SSD, Silver',
    product_description='Looking for some power? Laptops in our Achieve range have impressive specs, so you can work on creative projects and finalise serious business documents.',
    product_price=799.00,
    product_quantity=10,
    category=laptop,
    location=warehouse,
    productstatus=inStock,
    productcatalogue = mordecaiCatalogue
)


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
db.session.add(Quintus)

db.session.commit()

print("Added all items to the database")
