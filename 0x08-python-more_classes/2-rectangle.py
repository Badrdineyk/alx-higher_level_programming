#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle."""
    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle

        args:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)
