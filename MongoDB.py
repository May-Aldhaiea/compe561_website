import pymongo
from pymongo import MongoClient
from datetime import datetime
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

DB = MongoClient("mongodb://localhost:27017")
FlaskDB = DB['Flask']

items_Database = FlaskDB['items']
logger.debug("Initialising Items Data Base")

orders_Database = FlaskDB['order_history']
logger.debug("Initialising Order Data Base")

login_Database = FlaskDB['login']
logger.debug("Initialising Login Data Base")


def add_item(name: str, quantity: int, ID: str, category: str, price: int):
    newEntry = {'name': name, 'quantity': quantity, 'item ID': ID, 'catagory': category, 'price': price}
    items_Database.insert_one(newEntry)
    logger.info("Appended entry into Items Database")
    print(newEntry)
    # TL note: I didn't write this to the json file, if you want it too open the json file and write
    # json.dumps(newEntry) into the .json file


def add_order(ID_Order: int, user_Id: int, total_price: float, total_items_amount: int):
    today = datetime.today().strftime('%m/%d/%Y')
    newEntry = {'idorder_history': ID_Order, 'U_Id': user_Id, 'date': today, 'total price': total_price,
                'total_items_amount': total_items_amount}
    orders_Database.insert_one(newEntry)
    logger.info("Appended entry into Orders Database")
    print(newEntry)


def add_user(user_Id: int, user_name: str, user_password: str, email: str):
    newEntry = {'U_Id': user_Id, 'UserId': user_name, 'UserPassword': user_password, 'email': email}
    login_Database.insert_one(newEntry)
    logger.info("Appended entry into User Database")
    print(newEntry)


if __name__ == "__main__":
    add_user(69, 'Pat', 'wasHere', "LplusRatio@420.com")

    # cursor = items_Database.find({})
    # for document in cursor:
    #     print(document)
    #
    # cursor = orders_Database.find({})
    # for document in cursor:
    #     print(document)
    #
    # cursor = login_Database.find({})
    # for document in cursor:
    #     print(document)

    findThis = {'U_Id': 69}

    login_Database.delete_many(findThis)
