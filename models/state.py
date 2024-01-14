#!/usr/bin/python3
"""Module containing state Class"""

from models.base_model import BaseModel


class State(BaseModel):
    """Class containing the state"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializing the class"""
        super().__init__(*args, **kwargs)
