#!/usr/bin/python3


def remove_char_at(str, n):
    '''creates a copy of the string, removing the character at the position n'''
    s = ""
    if n > len(str) or n < 0:
        return str
    else:
        for letter in str:
            if letter != str[n]:
                s += letter
        return s
