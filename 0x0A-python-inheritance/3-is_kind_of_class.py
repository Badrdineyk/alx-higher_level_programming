#!/usr/bin/python3
"""Defines a class-checking function"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited of a class.

    args:
        obj: The object to check
        a_class: The class to be checked
    Returns:
        True if obj is an instance or inherited instance of a_class
        Otherwise False
    """
    return isinstance(obj, a_class)
