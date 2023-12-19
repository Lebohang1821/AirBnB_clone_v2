#!/usr/bin/python3
""" """
from models.review import Review
from tests.test_models.test_base_model import test_basemodel
import os


class test_review(test_basemodel):
    """ It reviews test class"""

    def __init__(self, *args, **kwargs):
        """ It reviews the class init"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ It is testing review place_id attr"""
        new = self.value()
        self.assertEqual(type(new.place_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_user_id(self):
        """ it test review user_id attr"""
        new = self.value()
        self.assertEqual(type(new.user_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_text(self):
        """ It is testing review text attr"""
        new = self.value()
        self.assertEqual(type(new.text), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
