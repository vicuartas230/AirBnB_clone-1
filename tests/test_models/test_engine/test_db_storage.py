#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel, Base
from models import storage
from models.engine import db_storage
from models.state import State
import models
import os
import pep8
from os import environ

DBStorage = db_storage.DBStorage
storage_type = environ["HBNB_TYPE_STORAGE"]


class test_db_storage(unittest.TestCase):
    """ Class to test the file storage method """
    @unittest.skipIf(storage_type != 'db', "no testing db storage")
    def test_all_returns_dict(self):
        """ Test returns a dictionaty """
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(storage_type != 'db', "no testing db storage")
    def test_all_no_class(self):
        """ Test returns all rows when no class is passed """

    @unittest.skipIf(storage_type != 'db', "no testing db storage")
    def test_new(self):
        """ Test new adds an object to the database """

    @unittest.skipIf(storage_type != 'db', "no testing db storage")
    def test_save(self):
        """ Test save properly saves objects to file.json """

    @unittest.skipIf(storage_type != 'db', "no testing db storage")
    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    @unittest.skipIf(storage_type != 'db', "no testing db storage")
    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        print(type(new))
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    @unittest.skipIf(storage_type != 'db', "no testing db storage")
    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = State("Antioquia")
        storage.new(new)
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    @unittest.skipIf(storage_type != 'db', "no testing db storage")
    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    @unittest.skipIf(storage_type != 'db', "no testing db storage")
    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_pep8_db_storage(self):
        """ Test models/engine/db_storage.py PEP8 """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_test_db_storage(self):
        """ Test tests/test_models/test_db_storage.py PEP8 """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
        test_db_storage.py'])
        self.assertEqual(result.total_errors, 1)

    def test_db_storage_class_docstring(self):
        """ Test the DBStorage class docstring """
        self.assertIsNot(DBStorage.__doc__, None)
        self.assertTrue(len(DBStorage.__doc__) >= 1)
