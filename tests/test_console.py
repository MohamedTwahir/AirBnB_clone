#!/usr/bin/python3
"""Test for my console"""

import unittest
import console
from console import HBNBCommand


class test_console(unittest, TestCase):
    """Console class"""

    def create(self):
        """instance Method"""
        return HBNBCommand()

    def test_quit(self):
        """Testing quit method"""
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        """Testing EOF method"""
        self.assertTrue(con.onecmd("EOF"))
