#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from models import user
from os import environ
import pep8
import unittest
User = user.User
storage_type = environ["HBNB_TYPE_STORAGE"]


class test_User(unittest.TestCase):
    """ Test User """

    def test_email_attr(self):
        """ Test User has attr email, and it's an empty string """
        user = User()
        self.assertTrue(hasattr(user, "email"))
        if storage_type == "db":
            self.assertEqual(user.email, None)
        else:
            self.assertEqual(user.email, None)

    def test_password_attr(self):
        """ Test User has attr password, and it's an empty string """
        user = User()
        self.assertTrue(hasattr(user, "password"))
        if storage_type == "db":
            self.assertEqual(user.password, None)
        else:
            self.assertEqual(user.password, None)

    def test_first_name_attr(self):
        """ Test User has attr first_name, and it's an empty string """
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        if storage_type == "db":
            self.assertEqual(user.first_name, None)
        else:
            self.assertEqual(user.first_name, None)

    def test_last_name_attr(self):
        """ Test User has attr last_name, and it's an empty string """
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        if storage_type == "db":
            self.assertEqual(user.last_name, None)
        else:
            self.assertEqual(user.last_name, None)


class TestUserDocs(unittest.TestCase):
    """ Test user documentation and pep8 """

    def test_pep8_user(self):
        """ Test models/user.py PEP8 """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_test_user(self):
        """ Test tests/test_models/test_state.py PEP8 """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring_user_module(self):
        """ Test user.py module docstring """
        self.assertIsNot(User.__doc__, None)
        self.assertTrue(len(User.__doc__) >= 1)

    def test_docstring_user_class(self):
        """Test user class docstring """
        self.assertIsNot(User.__doc__, None)
        self.assertTrue(len(User.__doc__) >= 1)
