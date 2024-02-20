#!/usr/bin/python3
"""Defines a file reading function"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout

    Args:
        filename (.txt): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as file:
        file_content = file.read()
        print(file_content)
