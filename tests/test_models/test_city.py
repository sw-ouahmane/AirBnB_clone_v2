#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """test for city"""

    def __init__(self, *args, **kwargs):
        """initialize"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """state id"""
        new = self.value(state_id="test")
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """name"""
        new = self.value(name="test")
        self.assertEqual(type(new.name), str)
