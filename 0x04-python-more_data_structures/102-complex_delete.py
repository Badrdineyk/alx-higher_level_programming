#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """deletes keys with a specific value in a dictionary."""
    keys = list(a_dictionary.keys())
    values = list(a_dictionary.values())

    if value not in values:
        return a_dictionary
    else:
        for i, v in enumerate(values):
            if v == value:
                del a_dictionary[keys[i]]
    return a_dictionary
