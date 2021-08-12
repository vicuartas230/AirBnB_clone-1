#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models import state
from os import environ
import models
import pep8
import unittest

State = state.State
storage_t = environ("HBNB_TYPE_STORAGE")


class test_state(test_basemodel):
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
        if storage_t == "db":
            self.assertEqual(state.name, None)
        else:
            self.assertEqual(state.name, None)
