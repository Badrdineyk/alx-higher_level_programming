#!/usr/bin/python3

def safe_print_integer(value):
    """prints an integer."""
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
