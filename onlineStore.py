import os
from app import create_app, db
from app.models import User, Product, ProductCatalogue, ShoppingBasket, Order

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Product=Product, Category=Category, Location=Location, ProductStatus=ProductStatus, ProductCatalogue=ProductCatalogue, ShoppingBasket=ShoppingBasket, Order=Order)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
