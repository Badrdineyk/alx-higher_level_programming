#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda item: [i ** 2 for i in item], matrix))
