#!/usr/bin/python3
"""Defines an object attribute lookup function"""


def lookup(obj):
    """returns the list of attributes and methods of an object

    args:
        obj: The object.
    """
    return dir(obj)
