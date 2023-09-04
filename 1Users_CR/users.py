from mysqlconnection import connectToMySQL
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):#noticed how cls is not used in this function
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)#this in needed to save and execute the connection between sql and here
        print(results)
        users= []
        for i in results:
            users.append( cls(i) )
        return users

    @classmethod
    def save(cls, request):#cls is the class inherited itself. You need another variable inside
        query = '''INSERT INTO users (first_name,last_name,email) 
        VALUES (%(first_name)s,%(last_name)s,%(email)s);'''
        results = connectToMySQL('users_schema').query_db(query,request)#this is reading request
        print(results)
        return results
