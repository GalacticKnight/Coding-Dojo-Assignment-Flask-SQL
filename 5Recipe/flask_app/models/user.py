from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash#incorperates the idea of an error alert when there is a mistake like catch and exception
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask_app import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)



class User:
    database="recipetest"#this is the schema!!!!!!
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email= data['email']
        self.password= data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #you know what is classmethod based on what you return!!!!
    #class is good for retreiveing information!!!
    #static is good for arithmetic!!!

    @classmethod
    def create_account(cls,data):#why cls is being thrown in the first place? !!!!!!
        query='''INSERT into users (first_name, last_name,email, password)
        VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);'''



        
        #WHEN YOU INSERT SOMETHING, AN ID IS GENERATED IN THE TABLE AND IT GETS SAVED IN THE RESULTS AND THATS WHAT IS BEING RETURNED!!!!!!!
        results = connectToMySQL(cls.database).query_db(query,data)
        return results

    #come back here
    @classmethod#we are going to make a new dictionary from this session variable and we are going to return a user. because this user will determine which account to open!!!!!
    def find_by_id(cls, data):#once it gets through validation, we can use this method to retreive that email name and save it as a user!!!!!!
        query='''SELECT * FROM users WHERE id= %(id)s'''
        results = connectToMySQL(cls.database).query_db(query,data)
        print(results)
        return cls(results[0])#we need to pull the first information from this dictionary!!!!!


    @classmethod
    def find_by_email(cls, data):#once it gets through validation, we can use this method to retreive that email name and save it as a user!!!!!!
        query='''SELECT * FROM users WHERE email= %(email)s'''
        results = connectToMySQL(cls.database).query_db(query,data)
        print(results)
        return cls(results[0])#we need to pull the first information from this dictionary!!!!!


    #when you use static method, you have to use the class name while if you use classmethod, you have to cls!!!!
    @staticmethod#this enables us to use this method without having to create a new instance!!!!!
    def validate_register(data):
        is_valid = True 
        query='''SELECT * FROM users WHERE email= %(email)s'''
        results = connectToMySQL(User.database).query_db(query,data)#why use user in the user.database!!!!!!
        if len(results) >= 1:#this is how we deteremine if email is already taken!!!!!
            flash("this email is already taken","register")#the ,"register") will only activate with register!!!!!!
            is_valid = False
        if len(data['first_name']) < 3:
            flash("At least 3 characters.","register")
            is_valid = False
        if len(data['last_name']) < 3:
            flash("At least 3 characters.","register")
            is_data = False
        if not EMAIL_REGEX.match(data['email']):#this is important!!!!!!!!
            flash("invalid email","register")
            is_data = False
        if len(data['password']) < 8:
            flash("Must have more than 8 characters.","register")
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash("Must confirm your password correctly.","register")
            is_valid = False
        return is_valid


    @staticmethod#this enables us to use this method without having to create a new instance!!!!!
    def validate_login(data):
        is_valid = True 
        query='''SELECT * FROM users WHERE email= %(email)s'''
        results = connectToMySQL(User.database).query_db(query,data)#(User.database)
        if results:
            found= User(results[0])#so we are putting results into a User. and saving it as found!!!!!!
            #why put 0? because you are getting back a list of dictionaries which in reality its just the first one!!!!!
            if not bcrypt.check_password_hash(found.password, data['password']):#so found.password,data['password'] is being hashed and checking to see if they are equal!!!!!!!
                flash("hash password does not match")
                is_valid=False
        else:#if we dont find a match then the follwoing activates!!!!!
            flash("we havent found a match","login")#the ,"login") will only activate with register!!!!!!
            is_valid = False
        return is_valid
    

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.database).query_db(query)
        results = []
        for i in results:
            users.append(cls(i))
        return users

    
    # query='''SELECT * FROM users WHERE email= %(email)s'''
        # results = connectToMySQL(database).query_db(query,data)
        # if not results:#if we dont find a match then the follwoing activates!!!!!