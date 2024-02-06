#!/usr/bin/python3
"""Defines a class Square:"""


class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """Initializes a new square

        args:
            size (int): size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """"Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size
