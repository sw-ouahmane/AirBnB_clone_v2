#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """Test for User"""

    def __init__(self, *args, **kwargs):
        """Initialize tests"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """test first name"""
        new = self.value(first_name="John")
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """test last name"""
        new = self.value(last_name="Doe")
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """test email"""
        new = self.value(email="test@test.com")
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """test password"""
        new = self.value(password="test")
        self.assertEqual(type(new.password), str)
