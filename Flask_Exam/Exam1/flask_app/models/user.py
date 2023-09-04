from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app.models import sighting
import re
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
database = "EXAM1"
class User:
    def __init__(self,user):
        self.id = user["id"]
        self.first_name = user["first_name"]
        self.last_name = user["last_name"]
        self.email = user["email"]
        self.password = user["password"]
        self.created_at = user["created_at"]
        self.updated_at = user["updated_at"]

    @classmethod
    def get_by_id(cls, user_id):
        data = {"id": user_id}
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(database).query_db(query,data)
        return result
    @classmethod
    def get_all(cls):
        query = "SELECT * from users;"
        user_data = connectToMySQL(database).query_db(query)
        users = []
        for user in user_data:
            users.append(cls(user))
        return users

    @classmethod
    def create_valid_user(cls, user):
        if not cls.is_new_account_valid(user):
            return False
        pw_hash = bcrypt.generate_password_hash(user['password'])# This scrambles the password using the generate function from BCrypst
        user = user.copy()
        user["password"] = pw_hash#then it saves it in password 
        print("User after adding pw: ", user)
        query = """
                INSERT into users (first_name, last_name, email, password)
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"""
        new_user = connectToMySQL(database).query_db(query, user)
        return new_user
    @classmethod
    def is_new_account_valid(cls, user):
        valid = True
        if len(user["first_name"]) < 2:
            valid = False
            flash("Unless your name is I there should be no reason why your name should only have one letter")
        if len(user["last_name"]) < 2:
            valid = False
            flash("Same for your last name") 
        if not EMAIL_REGEX.match(user['email']): 
            flash("false email")
            valid = False
        if not user["password"] == user["password_confirmation"]:
            flash("Mine sharing your password with me? No worries, you can trust me hehe XD.")
            valid = False
        return valid