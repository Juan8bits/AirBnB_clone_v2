#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from models import user
import pep8
import unittest


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value(first_name="Betty")
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value(last_name="Holberton")
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value(email="imdev@holbertonschool.com")
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value(password="user123")
        self.assertEqual(type(new.password), str)


class Testpep8(unittest.TestCase):
    """Class to do pep8 validation. """
    def test_pep8(self):
        """Method to probe pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/user.py'
        file2 = 'tests/test_models/test_user.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found errors (or warnings).")


class TestDocs_for_file_storage_file(unittest.TestCase):
    """ Class to check documentation in files."""
    def test_module_doc(self):
        """Method to check for module documentation."""
        self.assertTrue(len(user.__doc__) > 0)

    def test_method_docs(self):
        """Method to check for method´s documentation."""
        for func in dir(User):
            self.assertTrue(len(func.__doc__) > 0)
