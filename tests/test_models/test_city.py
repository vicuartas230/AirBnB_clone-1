#!/usr/bin/python3
""" """
from models import city
from os import environ
import models
import pep8
import unittest

City = city.City
storage_type = environ["HBNB_TYPE_STORAGE"]


class test_City(unittest.TestCase):
    """ Test city """

    def test_name(self):
        """ Test City attribute name, empty string """
        city = City()
        self.assertTrue(hasattr(city, "name"))
        if storage_type == "db":
            self.assertEqual(city.name, None)
        else:
            self.assertEqual(city.name, None)

    def test_state_id(self):
        """ Test City attribute state_id, empty string """
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        if storage_type == "db":
            self.assertEqual(city.state_id, None)
        else:
            self.assertEqual(city.state_id, None)

    def test_to_dict(self):
        """ Test values in dict return from to_dict """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        c = City()
        new_d = c.to_dict()
        self.assertEqual(new_d["__class__"], "City")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], c.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], c.updated_at.strftime(t_format))


class TestCityDocs(unittest.TestCase):
    """ Test City documentation and pep8 """

    def test_pep8_city(self):
        """ Test models/city.py PEP8 """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_test_city(self):
        """ Test tests/test_models/test_review.py PEP8 """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring_city_module(self):
        """ Test city.py module docstring """
        self.assertIsNot(city.__doc__, None)
        self.assertTrue(len(city.__doc__) >= 1)

    def test_docstring_city_class(self):
        """Test city class docstring """
        self.assertIsNot(city.__doc__, None)
        self.assertTrue(len(city.__doc__) >= 1)
