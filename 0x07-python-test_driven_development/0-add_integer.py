#!/usr/bin/python3

"""Defines an integer addition function."""


def add_integer(a, b=98):
    """adds 2 integers and returns the addition.

    args:
    a (int or float): The first number to be added
    b (int or float): The second number to be added

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
