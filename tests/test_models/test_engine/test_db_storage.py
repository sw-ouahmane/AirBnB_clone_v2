#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
import unittest

DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        if models.storage_t == 'db':
            self.assertIs(type(models.storage.all()), dict)

    def test_get(self):
        """Test that get properly returns a requested object"""
        if models.storage_t == 'db':
            user = User(email="User1@mail.com", password='test')
            user.save()
            self.assertEqual(storage.get(User, user.id), user)

    def test_count(self):
        """Test that count properly counts all objects"""
        if models.storage_t == 'db':
            self.assertEqual(len(models.storage.all()), models.storage.count())