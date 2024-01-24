#!/usr/bin/python3

def best_score(a_dictionary):
    """returns a key with the biggest integer value."""
    if a_dictionary is None:
        return None

    keys_list = list(a_dictionary.keys())
    values_list = list(a_dictionary.values())

    max_score = max(values_list)
    idx = values_list.index(max_score)
    return keys_list[idx]
