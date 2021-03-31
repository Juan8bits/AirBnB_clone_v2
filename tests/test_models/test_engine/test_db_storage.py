#!/usr/bin/python3
"""Defines unnittests for models/engine/db_storage.py."""
import unittest
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from console import HBNBCommand
from models.engine.db_storage import DBStorage
import pep8


class Testpep8(unittest.TestCase):
    """Class to do pep8 validation. """

    def test_pep8(self):
        """Method to probe pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/engine/db_storage.py'
        file2 = 'tests/test_models/test_engine/test_db_storage.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found errors (or warnings).")
