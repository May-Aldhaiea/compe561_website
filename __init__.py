"""
This file serves as the initial point where all the required functions are carried out.
In other words, this is where the initalization takes place.

"""
#import the required modules
import sys
import os
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask import Flask
import mysql.connector

#initialize app
app = Flask(__name__)
#set the secret key
app.config["SECRET_KEY"] = "%$$###@@@@@@@secret"
#create database connection - this connection will be used in all other areas where connection to db is required
connection = mysql.connector.connect(host="localhost", port="3306", user="root", database="flask")
#initialize bcrypt - for password encryption
bcrypt = Bcrypt(app)
#initalize login manager - needed for checking auth status
login_manager = LoginManager(app)
#import the routes
from webapp import routes