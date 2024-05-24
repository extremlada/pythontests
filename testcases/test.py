import unittest
from unittest.mock import patch, mock_open
from readers.readingInCsv import *
from database.Database import *
from readers.ReadingCSV import *
from readers.ReadingJson import *

class TestingFileReaderCsv(unittest.TestCase):

    def test_wrong_file_type_and_wrong_file_path(self):
        with self.assertRaises(ValueError): read_file('asd', 'asd')
    def test_wrong_file_type(self):
        with self.assertRaises(ValueError):read_file('asd', 'readers/test.json'),
        with self.assertRaises(ValueError):read_file('asd', 'readers/test.csv')

    @patch('builtins.open', mock_open(read_data="Név, Város, Életkor \n József, Budapest, 20"))
    def test_read_csv(self):
        reading = CsvReader.read_csv('readers/test.csv')
        self.assertIsInstance(reading, Database)
        self.assertEqual(len(reading.data), 3)

    @patch('builtins.open', side_effect=FileNotFoundError('FileNotFoundException'))
    def test_bad_read_csv(self, mock_open):
        reading = CsvReader.read_csv('readers/test.json')
        self.assertIsInstance(reading, Database)
        self.assertEqual(len(reading.data), 3)

    @patch('builtins.open', mock_open(read_data='[{"Név":"József", "Város":"sebes", "Életkor":"20"}]'))
    def test_read_json(self):
        reading = JsonReader.read_json('readers/test.json')
        self.assertIsInstance(reading, Database)
        self.assertEqual(len(reading.data), 1)



if __name__ == "__main__":
    unittest.main()
