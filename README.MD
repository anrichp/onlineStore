# Online Store

You have been asked to design a software system for a well-known online store. The system will allow customers to search for products sold at the website and add them to their shopping basket - at this stage an order is in progress. Products are sold both by the website itself and several third-party sellers as part of the website’s marketplace. Third-party sellers can be individuals or organisations, and once they have registered as a seller, they maintain their own product catalogue, pricing and storefront. If a product is temporarily out of stock, then then it will be marked as unavailable.

Once a customer has finished their shopping, the order is considered to be processing and they are taken through the checkout process, where they will specify delivery details. Customers have the choice of several delivery options, including standard delivery using the postal service and the company’s own in-house courier service. Products ordered from third-party sellers at the marketplace do not have access to the in-house courier system. When the delivery options have been chosen, then the customer is presented with the payment options, where they can opt to use a credit or debit card, an online payment service (e.g., PayPal) or a gift voucher. Additionally, customers may also use promotional codes that are periodically issued by the website. Customers have the option to store their payment details and so can simply use stored details for each purchase. At this stage, the order is pending payment, but once the customer submits their payment information, the validity of the account used (whether it is PayPal, a credit/debit card or gift voucher) will be verified by the appropriate service. Upon successful completion, the order is awaiting picking.

When a customer completes a transaction, the order is passed to the warehouse staff. The warehouse staff will be required to look up the items on the stock database to determine the location of the item in the warehouse. Once the items are successfully collected and packaged, the order will be considered ready for delivery and distributed to the appropriate delivery company, depending on the customer’s preferences. When a member of the warehouse staff picks an item, to fulfil a customer order, the item is scanned with a handheld terminal to automatically update the stock levels (which will be reflected on the website). Finally, the order is collected by the appropriate delivery company and marked as shipped.

## Installation

### Update to the latest version of Python3

```
sudo apt-get install python3
```

### Install Dependencies

To run this project, you will need to run the requirements.txt file
listed in **dependencies** section below.

### Dependencies

```
pip3 install -r requirements.txt
```

## Create & Populate Database

- A database with the name **onlinestore** has been created in codio for this project.
  If you wish to run this project outside of codio, you will need to create a new MySQL database
  with the name **onlinestore** and modify the flask config.py file by modifying the connect string
  to reflect the newly created database.

```
export FLASK_APP=onlinestore.py
```

```
flask shell
```

```
import onlineStore
```

```
db.create_all()
```

```
import populateDB
```

## Run the Application

```
python3 onlineStore.py
```

To preview the application, please click on the Box URL Preview button in codio
<img src="/images/box url.png" alt="Preview button"/>

### Preview configuration

```
{
    // This file is used to configure the three buttons along Codio's top menu.
    // Run button configuration
    "commands": {
        "Run": "python3 {{filepath}}"
    },
    // Preview button configuration
    "preview": {
        "Project Index (static)": "https://{{domain}}/{{index}}",
        "Current File (static)": "https://{{domain}}/{{filepath}}",
        "Box URL": "http://{{domain5000}}/",
        "Box URL SSL": "https://{{domain3000}}/"
    },
    // Debugger target button configuration
    "debugger": [{
        "type": "PYTHON3",
        "command": "{{filepath}}",
        "before": "",
        "uuid": "6c228c3f-596c-c44a-399f-5d86a7e17bf9",
        "name": "Debug"
    }]
}
```
