#!/usr/bun/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """adds 2 tuples."""
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0

    a, b = tuple_a
    x, y = tuple_b

    return a + x, b + y
