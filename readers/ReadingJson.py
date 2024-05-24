import json
from database.Database import Database
from database.Person import Person

class JsonReader:
    @staticmethod
    def read_json(file_path):
        db = Database()
        try:
            with open(file_path, 'r', encoding='utf-8') as jsonfile:
                data = json.load(jsonfile)
                for entry in data:
                    if all(key in entry for key in ['Név', 'Város', 'Életkor']):
                        person = Person()
                        person.update_person(Név=entry['Név'], Város=entry['Város'], Életkor=entry['Életkor'])
                        db.add_person(person)
        except FileNotFoundError:
            print("File not found")
        return db
