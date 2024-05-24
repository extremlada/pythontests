from unittest.mock import patch, mock_open, MagicMock
import unittest
from database.DatabaseManager import DatabaseManager
from testcases.mocks.Filter import Filter
from database.Person import Person
from readers.readingInCsv import read_file


class Modified(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseManager()
        self.filter = Filter()
        self.filter.keep = MagicMock(name="keep")

    @patch("builtins.open", mock_open(read_data='[{"Név": "zsadány", "Város": "Budapest", "Életkor": "20"}]'))
    def test_modified_data(self):
        self.db.read_file('json', 'readers/test.json')
        entry_to_modify = "zsadány"
        newdict = {'Név': 'James'}
        self.assertTrue(self.db.modify_person(entry_to_modify, newdict))
