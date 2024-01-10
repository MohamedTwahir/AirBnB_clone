#!/usr/bin/python3
"""Module for user class inheriting from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class Inheriting from BaseModel."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
