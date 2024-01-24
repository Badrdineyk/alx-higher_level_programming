#!/usr/bin/python3

def best_score(a_dictionary):
    """returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    keys_list = list(a_dictionary.keys())
    values_list = list(a_dictionary.values())

    max_score = max(values_list)
    idx = values_list.index(max_score)

    return keys_list[idx]
