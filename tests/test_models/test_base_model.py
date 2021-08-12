#!/usr/bin/python3
""" """
from models import base_model
from os import environ
import models
import pep8
import unittest

BaseModel = base_model.BaseModel
storage_type = environ["HBNB_TYPE_STORAGE"]


class test_basemodel(unittest.TestCase):
    """ test Base Model """

    def test_str(self):
        """ Test the str method """
        instanc = BaseModel()
        string = "[BaseModel] ({}) {}".format(instanc.id, instanc.__dict__)
        self.assertEqual(string, str(instanc))

    def test_to_dict_values(self):
        """ Test values in dict return from to_dict """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        bm = BaseModel()
        new_d = bm.to_dict()
        self.assertEqual(new_d["__class__"], "BaseModel")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], bm.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], bm.updated_at.strftime(t_format))


class TestBaseDocs(unittest.TestCase):
    """ Test BaseModel documentation and pep8 """

    def test_pep8_base(self):
        """ Test models/base_model.py PEP8 """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_test_base(self):
        """ Test tests/test_models/test_base_model.py PEP8 """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring_base_module(self):
        """ Test base_model.py module docstring """
        self.assertIsNot(BaseModel.__doc__, None)
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_docstring_base_class(self):
        """ Test base_model class docstring """
        self.assertIsNot(BaseModel.__doc__, None)
        self.assertTrue(len(BaseModel.__doc__) >= 1)
