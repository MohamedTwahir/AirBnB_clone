#!/usr/bin/python3
"""Module containing amenity class"""

from models.base_model import BaseModel


class Amenity:
    """Class representing amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Amenity class Initialization"""
        super().__init__(*args, **kwargs)
