from unittest.mock import patch, mock_open, MagicMock
import unittest
from database.DatabaseManager import DatabaseManager, PersonNotFoundError
from testcases.mocks.Filter import Filter
from database.Person import Person
from readers.readingInCsv import read_file


import unittest
from unittest.mock import patch, Mock
from database.DatabaseManager import DatabaseManager

class TestDatabaseManager(unittest.TestCase):

    @patch('database.DatabaseManager.Database')
    @patch('database.Person')
    def test_modify_person_with_empty_new_data(self, mock_person, mock_db):
        mock_db.get_people_names.return_value = ['Alice', 'Bob', 'Charlie']
        mock_person.get_name.return_value = 'Alice'
        manager = DatabaseManager()

        with self.assertRaises(ValueError):
            manager.modify_person('Alice', {})

    @patch('database.DatabaseManager.Database')
    @patch('database.Person')
    def test_modify_person_with_existing_person(self, mock_person, mock_db):
        mock_db.get_people_names.return_value = ['Alice', 'Bob', 'Charlie']
        mock_person.get_name.return_value = 'Alice'
        manager = DatabaseManager()

        manager.modify_person('Alice', {'age': 30, 'city': 'New York'})
        self.assertTrue(mock_person.update_person.called)

    @patch('database.DatabaseManager.Database')
    @patch('database.Person')
    def test_modify_person_with_non_existing_person(self, mock_person, mock_db):
        mock_db.get_people_names.return_value = ['Alice', 'Bob', 'Charlie']
        mock_person.get_name.return_value = 'Alice'
        manager = DatabaseManager()

        with self.assertRaises(PersonNotFoundError):
            manager.modify_person('Dave', {'age': 30, 'city': 'New York'})

    @patch('database.DatabaseManager.Database')
    @patch('database.Person')
    def test_modify_person_with_non_existing_person_and_empty_new_data(self, mock_person, mock_db):
        mock_db.get_people_names.return_value = ['Alice', 'Bob', 'Charlie']
        mock_person.get_name.return_value = 'Alice'
        manager = DatabaseManager()

        with self.assertRaises(PersonNotFoundError):
            manager.modify_person('Dave', {})

    @patch('database.DatabaseManager.Database')
    @patch('database.Person')
    def test_modify_person_with_non_existing_person_and_invalid_new_data(self, mock_person, mock_db):
        mock_db.get_people_names.return_value = ['Alice', 'Bob', 'Charlie']
        mock_person.get_name.return_value = 'Alice'
        manager = DatabaseManager()

        with self.assertRaises(PersonNotFoundError):
            manager.modify_person('Dave', {'age': '30', 'city': 'New York'})