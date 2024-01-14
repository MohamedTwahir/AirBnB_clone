#!/usr/bin/python3
"""Module for initialization"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
