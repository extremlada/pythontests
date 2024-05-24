import csv
from database.Person import Person
from lekérések.get import *


class CsvReader:
    @staticmethod
    def read_csv(file_path):
        db = Database()
        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    person = Person()
                    person.update_person(Név = row['Név'], Város = row['Város'], Életkor= row['Életkor'])
        except (csv.Error, IOError) as e:
            print(f"file reading error: {e}")
            raise FileNotFoundError("FileNotFoundException")

        return db
