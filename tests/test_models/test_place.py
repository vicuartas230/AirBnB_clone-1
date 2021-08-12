#!/usr/bin/python3
""" """
from models import place
from os import environ
import models
import pep8
import unittest

Place = place.Place
storage_type = environ["HBNB_TYPE_STORAGE"]


class test_Place(unittest.TestCase):
    """ Test Places """

    def test_city_id(self):
        """ Test Place city_id, empty string """
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        if storage_type == "db":
            self.assertEqual(place.city_id, None)
        else:
            self.assertEqual(place.city_id, None)

    def test_user_id(self):
        """Test Place user_id, empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        if storage_type == "db":
            self.assertEqual(place.user_id, None)
        else:
            self.assertEqual(place.user_id, None)

    def test_name(self):
        """Test Place name, empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        if storage_type == "db":
            self.assertEqual(place.name, None)
        else:
            self.assertEqual(place.name, None)

    def test_description(self):
        """Test Place description, empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        if storage_type == "db":
            self.assertEqual(place.description, None)
        else:
            self.assertEqual(place.description, None)

    def test_number_rooms(self):
        """Test Place number_rooms, int == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        if storage_type == "db":
            self.assertEqual(place.number_rooms, None)
        else:
            self.assertEqual(place.number_rooms, None)

    def test_number_bathrooms(self):
        """Test Place number_bathrooms, int == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        if storage_type == "db":
            self.assertEqual(place.number_bathrooms, None)
        else:
            self.assertEqual(place.number_bathrooms, None)

    def test_max_guest(self):
        """Test Place max_guest, int == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        if storage_type == "db":
            self.assertEqual(place.max_guest, None)
        else:
            self.assertEqual(place.max_guest, None)

    def test_price_by_night(self):
        """Test Place price_by_night, int == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        if storage_type == "db":
            self.assertEqual(place.price_by_night, None)
        else:
            self.assertEqual(place.price_by_night, None)

    def test_latitude(self):
        """Test Place latitude, float == 0.0"""
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        if storage_type == "db":
            self.assertEqual(place.latitude, None)
        else:
            self.assertEqual(place.latitude, None)

    def test_longitude(self):
        """Test Place longitude, float == 0.0"""
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        if storage_type == "db":
            self.assertEqual(place.longitude, None)
        else:
            self.assertEqual(place.longitude, None)

    @unittest.skipIf(storage_type == 'db', "no testing File Storage")
    def test_amenity_ids_attr(self):
        """Test Place list amenity_ids, empty list"""
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(type(place.amenity_ids), list)
        self.assertEqual(len(place.amenity_ids), 0)

    def test_to_dict_values(self):
        """ Test values in dict return from to_dict """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(new_d["__class__"], "Place")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], p.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], p.updated_at.strftime(t_format))


class TestPlaceDocs(unittest.TestCase):
    """ Test Place documentation and pep8 """

    def test_pep8_place(self):
        """ Test models/place.py PEP8 """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_test_place(self):
        """ Test tests/test_models/test_place.py PEP8 """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring_place_module(self):
        """ Test place.py module docstring """
        self.assertIsNot(place.__doc__, None)
        self.assertTrue(len(place.__doc__) >= 1)

    def test_docstring_place_class(self):
        """Test place class docstring """
        self.assertIsNot(place.__doc__, None)
        self.assertTrue(len(place.__doc__) >= 1)
