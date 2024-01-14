#!/usr/bin/python3
"""Module containing Review class inherited from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class representing review"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Review Class Initialization"""
        super().__init__(*args, **kwargs)
