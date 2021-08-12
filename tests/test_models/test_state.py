#!/usr/bin/python3
""" """

from models import state
from os import environ
import models
import pep8
import unittest

State = state.State
storage_type = environ["HBNB_TYPE_STORAGE"]


class test_state(unittest.TestCase):
    """ Test State """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name_attr(self):
        """ Test State has attribute name, and it's as an empty string """
        state = State()
        self.assertTrue(hasattr(state, "name"))
        if storage_type == "db":
            self.assertEqual(state.name, None)
        else:
            self.assertEqual(state.name, None)


class TestStateDocs(unittest.TestCase):
    """ Test state documentation and pep8 """

    def test_pep8_state(self):
        """ Test models/state.py PEP8 """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_test_state(self):
        """ Test tests/test_models/test_state.py PEP8 """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring_state_module(self):
        """ Test state.py module docstring """
        self.assertIsNot(state.__doc__, None)
        self.assertTrue(len(state.__doc__) >= 1)

    def test_docstring_state_class(self):
        """Test State class docstring """
        self.assertIsNot(State.__doc__, None)
        self.assertTrue(len(State.__doc__) >= 1)
