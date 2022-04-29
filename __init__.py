import flask
from flask import url_for # don't get rid of this import
import database as db
app = flask.Flask(__name__)

itemsDB = db.get_items()
ordersDB = db.get_order()
loginDB = db.get_login()


@app.route('/home.html')
@app.route('/home')
@app.route('/')
def home():
    price = itemsDB[1]['price']
    return flask.render_template("home.html", testprice=price)


@app.route('/signup')
@app.route('/signup.html')
def signup():
    return flask.render_template("signup.html")

@app.route('/categories')
@app.route('/categories.html')
def categories():
    return flask.render_template("categories.html")


@app.route('/cart')
@app.route('/cart.html')
def cart():
    return flask.render_template("cart.html")

@app.route('/career')
@app.route('/career.html')
def career():
    return flask.render_template("career.html")

@app.route('/aboutUs')
@app.route('/aboutUs.html')
def aboutUs():
    return flask.render_template("aboutUs.html")

@app.route('/giftCard')
@app.route('/giftCard.html')
def giftCard():
    return flask.render_template("giftCard.html")

@app.route('/signin')
@app.route('/signin.html')
def signin():
    return flask.render_template("signin.html")

if __name__ == '__main__':
    app.debug = True
    app.run()