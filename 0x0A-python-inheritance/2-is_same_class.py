#!/usr/bin/python3
"""Defines a class-checking function"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a class.

    args:
        obj: The object to check
        a_class: The class to be checked
    Returns:
        True if the obj is an instance of a_class
        Otherwise False
    """
    if type(obj) is a_class:
        return True
    return False
