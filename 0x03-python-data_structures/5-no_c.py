#!/usr/bin/python3
def no_c(my_string):
    """removes all characters c and C from a string."""
    new_str = [char for char in my_string if char != 'c' and char != 'C']
    return ''.join(new_str)
