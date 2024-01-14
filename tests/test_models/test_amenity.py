#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
from datetime import datetime
from models.amenity import Amenity
import pep8
import json
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    """Test Cases for the Amenity class."""

    def test_doc_module(self):
        """Testing module documentation"""
        doc = Amenity.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_amenity(self):
        """Testing if module confers to PEP8"""
        pep8style = pep.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(
                result.total_errors, 0,
                "Found code style errors (and warnings)."
                )

    def test_pep8_conformance_amenity(self):
        """Testing if module confers to PEP8"""
        pep8style = pep.StyleGuide(quiet=True)
        res = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(
                res.total_errors, 0,
                "Found code style errors (and warnings)."
                )

    def test_doc_construction(self):
        """testing construction documentation"""
        doc = Amenity.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """Test for attributes validation"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Amenity, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Amenity.name, str)


if __name__ == "__main__":
    unittest.main()
