#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for a in matrix:
        new_matrix.append(list(map(lambda b: b**2, a)))
    return new_matrix
