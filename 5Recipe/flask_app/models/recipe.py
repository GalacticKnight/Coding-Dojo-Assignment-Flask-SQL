from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash#incorperates the idea of an error alert when there is a mistake like catch and exception
from flask_app.models.user import User#you want to add this so you can use the methods in models!!!!!!


class Recipe:
    database="recipetest"#this is the schema!!!!!!
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None# this results in blank in case nothing is there!!!!!

    @staticmethod
    def validate_recipe(data):
        is_valid = True 
        if len(data['name']) < 3:
            flash("At least 3 characters.")
            is_valid = False
        if len(data['description']) < 3:
            flash("At least 3 characters.")
            is_data = False
        if len(data['instructions']) < 3:
            flash("instructions")
            is_data = False
        return is_valid

    
    @classmethod
    def save(cls,data):#you need user_id!!!!!!
        query = '''INSERT INTO recipes (name, description,instructions, date_made, under_30, user_id) VALUES 
                                    (%(name)s, %(description)s, %(instructions)s,%(date_made)s, %(under_30)s, %(user_id)s);'''
        return connectToMySQL(cls.database).query_db(query,data)

    @classmethod
    def update(cls,data):#you need user_id!!!!!!
        query = '''UPDATE recipes SET 
        name = (%(name)s),description = (%(description)s),instructions = (%(instructions)s),date_made = (%(date_made)s),under_30 = (%(under_30)s) where id= %(id)s;'''
        return connectToMySQL(cls.database).query_db(query,data)


    @classmethod
    def delete(cls,data):
        query = '''DELETE FROM recipes WHERE ID = %(id)s;'''#??????????????????????
        results = connectToMySQL(cls.database).query_db(query,data)


    @classmethod#we are going to make a new dictionary from this session variable and we are going to return a user. because this user will determine which account to open!!!!!
    #this is find by recipe id
    def find_by_id(cls, data):#once it gets through validation, we can use this method to retreive that email name and save it as a user!!!!!!
        query='''SELECT * FROM recipes LEFT JOIN users on users.id = recipes.user_id WHERE recipes.id= %(id)s'''#!!!!!!!!!!!
        results = connectToMySQL(cls.database).query_db(query,data)
        print(results)
        r = cls(results[0])#we are creating a new recipe instance!!!!!!
        u = {#in this dictionary,for each instance of u, we are creating a users_id!!!!????????????????????????????
            "id": results[0]["users.id"],
            "first_name":results[0]["first_name"],
            "last_name":results[0]["last_name"],
            "email":results[0]["email"],
            "password":results[0]["password"],
            "created_at":results[0]["users.created_at"],
            "updated_at":results[0]["users.updated_at"]
        }#now that we have all the correct information from users, we can now create a user from this information.!!!!!!!!
        #for each i in result, we are creating a new r and u for results!!!!
        print(results)
        r.creator=User(u)#
        return r#we need to pull the first information from this dictionary!!!!!





# [{'id': 1, 'name': 'Cookie', 'description': 'chocolate chip', 'instructions': 'step 1', 'date_made': 
# datetime.datetime(2022, 12, 16, 22, 35, 21), 'under_30': 1, 'created_at': datetime.datetime(2022, 12, 16, 22, 35, 21), 
# 'updated_at': datetime.datetime(2022, 12, 16, 22, 35, 21), 'user_id': 3, 'users.id': 3, 'first_name': 'Vincent', 'last_name': 'Las', 
# 'email': 'test@test.com', 'password': '$2b$12$69JbTUxvoM.6qbNuxBe7.OVpFwEZPJPpxpONm4bNx67Nm7epVmhtS', 'users.created_at':
#  datetime.datetime(2022, 12, 16, 22, 9, 12), 'users.updated_at': datetime.datetime(2022, 12, 16, 22, 9, 12)}]
    @classmethod
    def get_all(cls):#the goal of this
        query = '''SELECT * FROM recipes
        LEFT JOIN users on users.id = recipes.user_id;'''
        results = connectToMySQL(cls.database).query_db(query)
        print(results)
        lst =[]#becomes all the recipes in the dictionary!!!!!
        for i in results:#for each one of i, we are creating a new recipe instance!!!!!!
            r = cls(i)#we are creating a new recipe instance!!!!!!
            u = {#in this dictionary,for each instance of u, we are creating a users_id!!!!????????????????????????????
                "id": i["users.id"],
                "first_name":i["first_name"],
                "last_name":i["last_name"],
                "email":i["email"],
                "password":i["password"],
                "created_at":i["users.created_at"],
                "updated_at":i["users.updated_at"]
            }#now that we have all the correct information from users, we can now create a user from this information.!!!!!!!!
            #for each i in result, we are creating a new r and u for results!!!!
            r.creator=User(u)#
            lst.append(r)
        return lst
