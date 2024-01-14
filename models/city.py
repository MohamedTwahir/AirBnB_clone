#!/usr/bin/python3
"""Module containing the City class"""

from models.base_model import BaseModel


class City:
    """class representing a city"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """City Class Initialization"""
        super().__init__(*args, **kwargs)
