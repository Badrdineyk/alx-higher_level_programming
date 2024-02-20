#!/usr/bin/python3
"""Defines append_after function."""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for.
        new_string (str): The string to insert.
    """
    txt = ""
    with open(filename) as r:
        for line in r:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)
