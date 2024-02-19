#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, attr_name, attr_value):
    """adds a new attribute to an object

    Args:
        obj (any): The object
        attr_name (str): The name of the attribute to be added
        attr_value (any): The value of the attribute
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
