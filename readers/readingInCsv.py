from readers.ReadingJson import *
from readers.ReadingCSV import *


class read_file:
    def __init__(self, file_type: str, file_path: str):
        self.file_type = file_type
        self.file_path = file_path
        try:
            if self.file_type == 'csv':
                self.db = CsvReader.read_csv(self.file_path)
            elif self.file_type == 'json':
                self.db = JsonReader.read_json(self.file_path)
            else:
                raise ValueError("Unsupported file type")
        except FileNotFoundError:
            print("File not found")


    def get_db(self):
        return self.db
