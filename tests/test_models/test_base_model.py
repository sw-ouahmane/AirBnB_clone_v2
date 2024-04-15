#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """Test for BaseModel"""

    def __init__(self, *args, **kwargs):
        """initialize"""
        super().__init__(*args, **kwargs)
        self.name = "BaseModel"
        self.value = BaseModel

    def setUp(self):
        """Setup"""
        pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_default(self):
        """default"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """kwargs int"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_str(self):
        """str"""
        i = self.value()
        f = "[{}] ({}) {}".format(self.name, i.id, i.__dict__)
        self.assertEqual(str(i), f)

    def test_todict(self):
        """to_dict"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """kwargs none"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """kwargs one"""
        n = {"Name": "test"}

    def test_id(self):
        """id"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """created_at"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """updated_at"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        # self.assertFalse(new.created_at == new.updated_at)
