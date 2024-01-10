#!/usr/bin/python3
"""Module containing Review class inherited from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class representing review"""
    place_id = ""
    user_id = ""
    text = ""
