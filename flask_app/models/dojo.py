from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    db = "dojos_and_ninjas_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        dojos = []
        for row in results:
            dojos.append(cls(row))
        return dojos

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(dojo_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        print("******", results)
        dojo = cls(results[0])
        print("*********", dojo)
        for row in results:
            ninja_data = {
                "id": row["ninjas.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "age": row["age"],
                "created_at": row["ninjas.created_at"],
                "updated_at": row["ninjas.updated_at"],
                "Dojo_id": row["Dojo_id"]
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo