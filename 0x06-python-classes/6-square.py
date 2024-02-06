#!/usr/bin/python3
"""Defines a class Square:"""


class Square:
    """Represent a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square

        args:
            size (int): size of the square.
            position (tuple):
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """"Get/set the current position"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
