#!/usr/bin/python3

def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple"""
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0

    numerator = 0
    denominator = 0
    for item in my_list:
        x, y = item
        numerator += (x * y)
        denominator += y
    avg = numerator / denominator
    return avg
