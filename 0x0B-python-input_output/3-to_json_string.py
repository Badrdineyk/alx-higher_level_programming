#!/usr/bin/python3
"""Defines to_json_string function"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)

    Args:
        my_obj (str): The object.
    """
    return json.dumps(my_obj)
