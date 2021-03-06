from app import db
from app.models import User, Customer, Orginisation, Product, Category, Location, ProductStatus, ProductCatalogue, Order, OrderLine, Orderstatus

# Create seller
sellerOrginisation = Orginisation(first_name='Anrich', last_name='Potgieter',
                                  email_address='anrichp@gmail.com', contact_number='07907451834',
                                  company_name='Mordecai', tax_certificate='1234')

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
    productcatalogue=mordecaiCatalogue
)
p2 = Product(
    product_title='LENOVO Legion 5P 15.6" Gaming Laptop - AMD Ryzen 7, RTX 2060, 256 GB SSD',
    product_description='Forget checking the game requirements - the RTX 2060 graphics card will play anything you throw at it. For unbelievably realistic lighting, shadows and reflections, the Turing architecture provides real-time ray tracing and AI-enhanced graphics.',
    product_price=849.87,
    product_quantity=10,
    category=laptop,
    location=warehouse,
    productstatus=inStock,
    productcatalogue=mordecaiCatalogue
)

p3 = Product(
    product_title='ACER Nitro 5 AN517 17.3" Gaming Laptop - Intel® Core™ i7, RTX 2060, 256 GB',
    product_description='In an intense gaming session the last thing you want is your hardware overheating. The Nitro 5 stays cool under pressure with dual fans, so you can finish off all your quests, missions and battles, no matter how long they take. And with the NitroSense app you can easily adjust and monitor fan speeds with one simple press of the hotkey.',
    product_price=849.87,
    product_quantity=10,
    category=laptop,
    location=warehouse,
    productstatus=inStock,
    productcatalogue=mordecaiCatalogue
)

o1 = Order(customer=Quintus, orderstatus=in_progress, total=1234)
line_item = OrderLine(order = o1, product=p1, quantity=1)

db.session.add(sellerOrginisation)
db.session.add(mordecaiCatalogue)
db.session.add(desktop)
db.session.add(laptop)
db.session.add(warehouse)
db.session.add(awaitingDelivery)
db.session.add(inStock)
db.session.add(outStock)
db.session.add(Quintus)
db.session.add_all([in_progress, processing, pending_payment,
                   awaiting_picking, ready_for_delivery, shipped])
db.session.add_all([p1, p2, p3])
db.session.add(o1)

db.session.commit()

print("Added all items to the database")
