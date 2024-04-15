#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """test for place"""

    def __init__(self, *args, **kwargs):
        """initialize"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """test city id"""
        new = self.value(city_id="test")
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """test user id"""
        new = self.value(user_id="test")
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """test name"""
        new = self.value(name="test")
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """test description"""
        new = self.value(description="test")
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """test number of rooms"""
        new = self.value(number_rooms=1)
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """test number of bathrooms"""
        new = self.value(number_bathrooms=1)
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """test max guest"""
        new = self.value(max_guest=1)
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """test price by night"""
        new = self.value(price_by_night=1)
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """test latitude"""
        new = self.value(latitude=1.1)
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """test longitude"""
        new = self.value(longitude=1.1)
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """test amenity ids"""
        new = self.value(amenity_ids=["test"])
        self.assertEqual(type(new.amenity_ids), list)
