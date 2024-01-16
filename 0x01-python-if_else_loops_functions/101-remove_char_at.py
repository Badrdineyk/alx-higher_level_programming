#!/usr/bin/python3
def remove_char_at(str, n):
    """Creates a copy of the str, removing the char at the position n"""
    if n < 0:
        return str
    else:
        return str[:n] + str[n+1:]
