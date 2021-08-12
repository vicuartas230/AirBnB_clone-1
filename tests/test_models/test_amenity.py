#!/usr/bin/python3
""" """
from models import amenity
from os import environ
import models
import pep8
import unittest

Amenity = amenity.Amenity
storage_type = environ["HBNB_TYPE_STORAGE"]


class test_Amenity(unittest.TestCase):
    """ Test Amenity """

    def test_name_attr(self):
        """Test Amenity name, empty string"""

        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        if storage_type == "db":
            self.assertEqual(amenity.name, None)
        else:
            self.assertEqual(amenity.name, None)

    def test_to_dict_values(self):
        """test values in dict return from to_dict"""

        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        amen = Amenity()
        new_d = amen.to_dict()
        self.assertEqual(new_d["__class__"], "Amenity")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"],
                         amen.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"],
                         amen.updated_at.strftime(t_format))


class TestAmenityDocs(unittest.TestCase):
    """ Test Amenity documentation and pep8 """

    def test_pep8_amenity(self):
        """ Test models/amenity.py PEP8 """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_test_amenity(self):
        """ Test tests/test_models/test_amenity.py PEP8 """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring_amenity_module(self):
        """ Test amenity.py module docstring """
        self.assertIsNot(amenity.__doc__, None)
        self.assertTrue(len(amenity.__doc__) >= 1)

    def test_docstring_amenity_class(self):
        """Test amenity class docstring """
        self.assertIsNot(amenity.__doc__, None)
        self.assertTrue(len(amenity.__doc__) >= 1)
