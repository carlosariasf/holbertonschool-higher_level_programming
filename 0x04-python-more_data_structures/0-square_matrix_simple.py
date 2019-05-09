#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = list()
    for row in matrix:
        matrix2.append([x*x for x in row])
    return matrix2
