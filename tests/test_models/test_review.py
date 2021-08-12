#!/usr/bin/python3
""" """
from models import review
from os import environ
import models
import pep8
import unittest

Review = review.Review
storage_type = environ["HBNB_TYPE_STORAGE"]


class test_review(unittest.TestCase):
    """ Test reviews """

    def test_place_id(self):
        """ Test Review attr place_id, empty string """
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        if storage_type == "db":
            self.assertEqual(review.place_id, None)
        else:
            self.assertEqual(review.place_id, None)

    def test_user_id(self):
        """ Test Review attr user_id, empty string """
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        if storage_type == "db":
            self.assertEqual(review.user_id, None)
        else:
            self.assertEqual(review.user_id, None)

    def test_text(self):
        """ Test Review attr text, empty string """
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        if storage_type == "db":
            self.assertEqual(review.text, None)
        else:
            self.assertEqual(review.text, None)

    def test_to_dict(self):
        """ Test values in dict return from to_dict """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        r = Review()
        new_d = r.to_dict()
        self.assertEqual(new_d["__class__"], "Review")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], r.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], r.updated_at.strftime(t_format))


class TestReviewsDocs(unittest.TestCase):
    """ Test Review documentation and pep8 """

    def test_pep8_review(self):
        """ Test models/review.py PEP8 """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_test_review(self):
        """ Test tests/test_models/test_review.py PEP8 """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring_review_module(self):
        """ Test review.py module docstring """
        self.assertIsNot(review.__doc__, None)
        self.assertTrue(len(review.__doc__) >= 1)

    def test_docstring_review_class(self):
        """Test review class docstring """
        self.assertIsNot(review.__doc__, None)
        self.assertTrue(len(review.__doc__) >= 1)
