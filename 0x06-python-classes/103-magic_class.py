#!/usr/bin/python3
"""Define a class that does exactly the same as the bytecode provided by ALX"""

import math


class MagicClass:
    """Represent a circle."""
    def __init__(self, radius=0):
        """initializes the class

        args:
            radius (int or float): The radius of the new MagicClass
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass."""
        return math.pi * self.__radius ** 2

    def circumference(self):
        """Return The circumference of the MagicClass."""
        return 2 * math.pi * self.__radius
