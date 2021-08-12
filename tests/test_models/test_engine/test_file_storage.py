#!/usr/bin/python3
""" Module for testing file storage"""
from models.engine.file_storage import FileStorage
from models.engine import file_storage
from os import environ
import models
import pep8
import unittest

FileStorage = file_storage.FileStorage
storage_type = environ["HBNB_TYPE_STORAGE"]


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """
    @unittest.skipIf(storage_type == 'db', "no testing file storage")
    def test_all_returns_dict(self):
        """Test  return the FileStorage.__objects"""
        storage = FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, storage._FileStorage__objects)


class TestFileStorageDocs(unittest.TestCase):
    """ Test Place documentation and pep8 """

    def test_pep8_FileStorage(self):
        """ Test models/engine/file_storage.py PEP8 """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_test_FileStorage(self):
        """ Test tests/test_models/test_engine/test_storage.py PEP8 """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(
            ['tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring_FileStorage_module(self):
        """ Test file_storage.py module docstring """
        self.assertIsNot(file_storage.__doc__, None)
        self.assertTrue(len(file_storage.__doc__) >= 1)

    def test_docstring_FileStorage_class(self):
        """Test FileStorage class docstring """
        self.assertIsNot(file_storage.__doc__, None)
        self.assertTrue(len(file_storage.__doc__) >= 1)
