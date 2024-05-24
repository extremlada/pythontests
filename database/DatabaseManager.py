import copy

from database.Database import Database
from readers.ReadingJson import JsonReader
from readers.ReadingCSV import CsvReader
from database.observer import *
from database.Person import Person
class UnsupportedFileTypeError(Exception):
    pass

class FileNotFoundError(Exception):
    pass

class PersonNotFoundError(Exception):
    pass

class DatabaseManager:
    def __init__(self):
        self.db = Database()
        self.persons = Person()
        self.subject = Subject()

    def read_file(self, file_type: str, file_path: str):
        try:
            if file_type == 'csv':
                self.db = CsvReader.read_csv(file_path)
            elif file_type == 'json':
                self.db = JsonReader.read_json(file_path)
            else:
                raise ValueError("Unsupported file type")
        except FileNotFoundError:
            print("File not found")
            return None
        else:
            return self.db

    def get_person(self, custom_filter) -> list:
        if custom_filter():
            return [person for person in self.db.get_people_names() if custom_filter(person)]

    def modify_person(self, person_name: str, new_data: dict):
        for person in self.db.get_people_names():
            if person == person_name:
                self.persons.update_person(**new_data)
                return True
        else:
            raise PersonNotFoundError(f"Person with name {person_name} not found")

    def add_observer(self, who: str, obs: Observer) -> None:
        person = next((person for person in self.db.data if self.persons.get_name() == who), None)
        if person:
            person.subscriber(obs)
        else:
            raise PersonNotFoundError(f"Person with name {who} not found")
