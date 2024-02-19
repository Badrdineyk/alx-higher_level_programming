#!/usr/bin/python3
"""Defines a class that inherits from list"""


class MyList(list):
    """Implements sorted method"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
