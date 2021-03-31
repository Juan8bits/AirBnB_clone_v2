#!/usr/bin/python3
"""Defines unnittests for models/engine/db_storage.py."""
import unittest
import MySQLdb
import models
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from console import HBNBCommand
from models.engine.db_storage import DBStorage
from models.engine import db_storage
from models.engine.file_storage import FileStorage
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.engine.base import Engine
import pep8


class TestDBStorage(unittest.TestCase):
    """ Unittests for testing the DBStorage class. """
    @classmethod
    def setUpClass(cls):
        """DBStorage testing setup.
        Instantiate new DBStorage.
        Fill DBStorage test session with instances of all classes.
        """
        if type(models.storage) == DBStorage:
            cls.storage = DBStorage()
            Base.metadata.create_all(cls.storage._DBStorage__engine)
            Session = sessionmaker(bind=cls.storage._DBStorage__engine)
            cls.storage._DBStorage__session = Session()
            cls.state = State(name="California")
            cls.storage._DBStorage__session.add(cls.state)
            cls.city = City(name="San_Jose", state_id=cls.state.id)
            cls.storage._DBStorage__session.add(cls.city)
            cls.user = User(email="poppy@holberton.com", password="betty")
            cls.storage._DBStorage__session.add(cls.user)
            cls.place = Place(city_id=cls.city.id, user_id=cls.user.id,
                              name="School")
            cls.storage._DBStorage__session.add(cls.place)
            cls.amenity = Amenity(name="Wifi")
            cls.storage._DBStorage__session.add(cls.amenity)
            cls.review = Review(place_id=cls.place.id, user_id=cls.user.id,
                                text="stellar")
            cls.storage._DBStorage__session.add(cls.review)
            cls.storage._DBStorage__session.commit()


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


class TestDocs_for_file_storage_file(unittest.TestCase):
    """ Class to check documentation in files."""
    def test_module_doc(self):
        """Method to check for module documentation."""
        self.assertTrue(len(db_storage.__doc__) > 0)

    def test_method_docs(self):
        """Method to check for method´s documentation."""
        for func in dir(DBStorage):
            self.assertTrue(len(func.__doc__) > 0)
