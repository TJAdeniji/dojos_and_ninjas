from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def getNinja(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for ninja in results:
            ninja.append(cls(ninja))
        return ninjas

    @classmethod
    def addNinja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, created_at, updated_at, dojo_id) VALUES (%(first_name)s, %(last_name)s, NOW(), NOW(), %(dojo_id)s);"

        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
