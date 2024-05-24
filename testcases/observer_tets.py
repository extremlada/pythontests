import unittest
from unittest.mock import Mock
from database.DatabaseManager import DatabaseManager, PersonNotFoundError


class TestDatabaseManager(unittest.TestCase):

    def setUp(self):
        self.db_manager = DatabaseManager()
        self.mock_observer = Mock()

    def test_add_observer_existing_person(self):
        self.db_manager.db.data = [{'name': 'Alice', 'subscribers': []}]
        self.db_manager.persons.get_name.return_value = 'Alice'

        self.db_manager.add_observer('Alice', self.mock_observer)

        self.db_manager.db.data[0]['subscribers'].append(self.mock_observer)
        self.db_manager.persons.get_name.assert_called_once_with()
        self.mock_observer.subscriber.assert_called_once_with(self.db_manager.db.data[0])

    def test_add_observer_non_existing_person(self):
        self.db_manager.db.data = [{'name': 'Bob', 'subscribers': []}]
        self.db_manager.persons.get_name.return_value = 'Alice'

        with self.assertRaises(PersonNotFoundError):
            self.db_manager.add_observer('Alice', self.mock_observer)

    def test_add_observer_empty_db(self):
        self.db_manager.db.data = []
        self.db_manager.persons.get_name.return_value = 'Alice'

        with self.assertRaises(PersonNotFoundError):
            self.db_manager.add_observer('Alice', self.mock_observer)

    def test_add_observer_no_person_data(self):
        self.db_manager.db.data = [{'subscribers': []}]
        self.db_manager.persons.get_name.return_value = 'Alice'

        with self.assertRaises(PersonNotFoundError):
            self.db_manager.add_observer('Alice', self.mock_observer)

    def test_add_observer_no_person_name(self):
        self.db_manager.db.data = [{'name': 'Alice', 'subscribers': []}]
        self.db_manager.persons.get_name.return_value = None

        with self.assertRaises(PersonNotFoundError):
            self.db_manager.add_observer('Alice', self.mock_observer)