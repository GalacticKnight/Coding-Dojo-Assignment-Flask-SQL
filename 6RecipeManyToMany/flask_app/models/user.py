from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash#incorperates the idea of an error alert when there is a mistake like catch and exception
from flask_app import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

class User:
    database="chatting"
    def __init__(self,data):
        self.id = database[id]
        self.firstname = data[firstname]
        self.lastname = data[lastname]
        self.password = data[password]
        self.email = data[email]
        self.created_at = data[created_at]
        self.updated_at = data[updated_at]
    
    #for you to make a login/reg, you just have a function that saves the reg information 
    def create_account(database):
        query='''INSERT into users (firstname, lastname, password,email)
        VALUES (%(firstname)s,%(lastname)s,%(password)s,%(email)s);'''
        results = connectToMySQL(cls.database).query_db(query,data)
        return results

    def validate_login(data):
        return


