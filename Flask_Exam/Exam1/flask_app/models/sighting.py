from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app.models import user
import re
database = "EXAM1"
class Sighting:
    def __init__(self, sighting):
        self.id = sighting["id"]
        self.location = sighting["location"]
        self.description = sighting["description"]
        self.spot_time = sighting["spot_time"]
        self.quantity = sighting["quantity"]
        self.created_at = sighting["created_at"]
        self.updated_at = sighting["updated_at"]
        self.user_id = None
    @classmethod
    def create_valid_sighting(cls, sighting_dict):
        if not cls.is_valid(sighting_dict):
            return False
        query = """INSERT INTO sightings (location, description, spot_time, quantity, user_id) 
        VALUES (%(location)s, %(description)s, %(spot_time)s, %(quantity)s, %(user_id)s);"""
        sighting = connectToMySQL(database).query_db(query, sighting_dict)
        return sighting
    @classmethod
    def delete_sighting_by_id(cls, sighting_id):
        query = "DELETE from sightings WHERE id = %(id)s;"
        sighting = connectToMySQL(database).query_db(query,data)
        return sighting
    @classmethod
    def update_sighting(cls, sighting_dict, session_id):
        query = """UPDATE sightings
                    SET name = %(name)s, description = %(description)s, instructions = %(spot_time)s, date_made=%(quantity)s
                    WHERE id = %(id)s;"""
        sighting = connectToMySQL(database).query_db(query,sighting_dict)
        return sighting

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sightings;"
        results = connectToMySQL(database).query_db(query)
        sightings = []
        for i in results:
            sightings.append(cls(i))
        return results
    @staticmethod
    def is_valid(sighting_dict):
        valid = True
        if len(sighting_dict["location"]) < 0:
            flash("Location field is required and must be at least 3 characters.")
            valid = False
        if len(sighting_dict["description"]) < 3:
            flash("You barely have anything")
            valid = False
        if len(sighting_dict["date_made"]) <= 0:
            flash("You date input is not correct")
            valid = False
        if len(sighting_dict["quantity"]) <= 0:
            flash("How could you even report a sasuqash if you havent even seen one??????? You troll")
            valid = False
        return valid