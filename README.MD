# Online Store

Item Catalog is a web application that provides a list of items
within a variety of categories and integrates third party
user registration and authentication. Authenticated users
should have the ability to post, edit, and delete their own items.

## Installation

Download the Latest version of Python

- Download Python [here](https://www.python.org/downloads/)

### Install Dependencies

To run this project, you will need to run the requirements.txt file
listed in **dependencies** section below.

### Dependencies

```
pip3 install -r requirements.txt
```

## Create & Populate Database

- A database with the name **onlinestore** has been created in codio for this project. If you wish to run this project outside of codio, you will need to create a new MySQL database with the name **onlinestore** and modify the flask config.py file and modify the connect string to reflect the newly created database.

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
