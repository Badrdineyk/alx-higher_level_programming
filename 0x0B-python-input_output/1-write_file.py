#!/usr/bin/python3
"""Defines a write-file function"""


def write_file(filename="", text=""):
    """writes a string to a text file.

    Args:
        filename (str): The name of the file to read.
        text (str): The text to be written
    Return:
        returns the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
