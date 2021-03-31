#!/usr/bin/python3
""" This is test for console.py"""
import unittest
import os
import pep8
import console
from models.base_model import BaseModel
from console import HBNBCommand
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """
    Unittesting class
    """

    def setUp(self):
        """ preparing the test """
        self.consol = HBNBCommand()

    def tearDown(self):
        """ after the setUp the test case is cleaned """
        pass

    def test_doc(self):
        """
        Tests if everything is documented
        """
        #  Module check
        self.assertIsNotNone(console.__doc__)

        #  Class check
        self.assertIsNotNone(HBNBCommand.__doc__)

        # Methods check
        for method in dir(HBNBCommand):
            self.assertIsNotNone(method.__doc__)


class Testpep8(unittest.TestCase):
    """Class to do pep8 validation. """
    def test_pep8(self):
        """Method to probe pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        file1 = 'console.py'
        file2 = 'tests/test_console.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found errors (or warnings).")
