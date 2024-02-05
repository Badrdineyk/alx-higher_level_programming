#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """executes a function safely."""
    try:
        div = fct(*args)
        return div
    except (ZeroDivisionError, IndexError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
