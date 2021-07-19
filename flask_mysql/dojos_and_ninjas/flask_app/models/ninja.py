from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import dojo

class Ninja: 
    def __init__(self, data):
        self.id = data['id']
        if "dojo_id" in data:
             self.dojo = dojo.Dojo.get_one({"id" : data['dojo_id']})
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) 
            VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s);
        """
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)

        all_ninjas = []

        for row in results:
            all_ninjas.append(cls(row))

        return all_ninjas

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)

        return cls(results[0])
