from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja 

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def getDojo(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def addDojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def getDojosWithNinjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        dojoData = cls(results[0])
        for row in results:
            ninja = {
                'id' : row['ninjas.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'], 
                'created_at' : row['ninjas.created_at'],
                'updated_at' : row['ninjas.updated_at']
            } 
        dojoData.ninjas.append(Ninja(ninja))
        return dojoData