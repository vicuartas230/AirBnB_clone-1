#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from models import user
from os import environ
import pep8
import unittest
User = user.User
storage_t = environ("HBNB_TYPE_STORAGE")


class test_User(test_basemodel):
    """ Test User """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_email_attr(self):
        """ Test User has attr email, and it's an empty string """
        user = User()
        self.assertTrue(hasattr(user, "email"))
        if storage_t == "db":
            self.assertEqual(user.email, None)
        else:
            self.assertEqual(user.email, None)

    def test_password_attr(self):
        """ Test User has attr password, and it's an empty string """
        user = User()
        self.assertTrue(hasattr(user, "password"))
        if storage_t == "db":
            self.assertEqual(user.password, None)
        else:
            self.assertEqual(user.password, None)

    def test_first_name_attr(self):
        """ Test User has attr first_name, and it's an empty string """
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        if storage_t == "db":
            self.assertEqual(user.first_name, None)
        else:
            self.assertEqual(user.first_name, None)

    def test_last_name_attr(self):
        """ Test User has attr last_name, and it's an empty string """
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        if storage_t == "db":
            self.assertEqual(user.last_name, None)
        else:
            self.assertEqual(user.last_name, None)
