import json
from datetime import datetime


with open(r"Database/items.json", "r") as f:
    items = json.loads(f.read())

with open(r"Database/order_history.json", "r") as f:
    orderHistory = json.loads(f.read())

with open(r"Database/usernameandpassworddemo.json", "r") as f:
    loginData = json.loads(f.read())


def add_item(name: str, quantity: int, ID: str, category: str, price: int):
    newEntry = {'name': name, 'quantity': quantity, 'item ID': ID, 'catagory': category, 'price': price}
    items.append(newEntry)
    # TL note: I didn't write this to the json file, if you want it too open the json file and write
    # json.dumps(newEntry) into the .json file


def add_order(ID_Order: int, user_Id: int, total_price: float, total_items_amount: int):
    today = datetime.today().strftime('%m/%d/%Y')
    newEntry = {'idorder_history': ID_Order, 'U_Id': user_Id, 'date': today, 'total price': total_price,
                'total_items_amount': total_items_amount}
    orderHistory.append(newEntry)


def add_user(user_Id: int, user_name: str, user_password: str, email: str):
    newEntry = {'U_Id': user_Id, 'UserId': user_name, 'UserPassword': user_password, 'email': email}
    loginData.append(newEntry)


def get_items() -> list:
    return items


def get_order() -> list:
    return orderHistory


def get_login() -> list:
    return loginData

# testing
# add_order(69, 70, 69.69, 420)
#
# print(orderHistory[-1])
# print(items[1]['price'])



