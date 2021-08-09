#!/usr/bin/python3
""" This script defines a class test_console """
import unittest
from console import HBNBCommand


class test_console(unittest.TestCase):
    """ This class defines all test for the console """

    def test_do_create(self):
        """ Test console create """
        HBNBCommand.do_create(
            self, 'Place city_id="0001" user_id="0001" \
name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 \
price_by_night=300 latitude=37.773972 longitude=-122.431297')
