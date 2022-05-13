"""
This file contains the database models. A model denotes a database model/table row
Each model has attributes - columns

"""
#imports
from webapp import app,connection
from webapp import login_manager
from flask_login import UserMixin
import random

#check the user login status
@login_manager.user_loader
def load_user(id):
    #create the cursor 
     cursor = connection.cursor(buffered=True)
     #execute the query
     cursor.execute("""SELECT * FROM users WHERE id = %s""", (id,))
     #fetch a single row
     data = cursor.fetchone()
     #check if a record was found
     if data:
        u = User(data[0],data[1],data[2])
        #return a user object mapped on the database record
        return u
     else:
        #no row found so return None
        return None


#user model 
class User:
    #constructor 
    def __init__(self,id, email, password):
      self._id = id
      self._email = email
      self._password = password
      self.authenticated = True
    
    #gets the id
    def get_id(self):
        return self._id
    
    #password property 
    @property
    def password(self):
        return self._password
    
    #email property
    @property
    def email(self):
        return self._email
    #active status
    def is_active(self):
        return True
    #authentication status
    @property
    def is_authenticated(self):
        return self.authenticated
    #user type status
    def is_anonymous(self):
        return False
    
    #static method to load user by email
    @staticmethod
    def find_user_by_email(email):
        cursor = connection.cursor(buffered=True)
        cursor.execute("""SELECT * FROM users WHERE email = %s""", (email,))
        data = cursor.fetchone()
        if data:
            u = User(data[0],data[1],data[2])
            return u
        else:
            return None
        
    #string representation of User class
    def __repr__(self):
        result = f'id : {self._id}, email : {self._email}, password : {self._password}'
        return result