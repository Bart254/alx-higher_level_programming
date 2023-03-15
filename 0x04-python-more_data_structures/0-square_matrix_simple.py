#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        square_list = []
        for e in matrix:
            square_list.append(list(map(lambda a: a * a, e)))
        return square_list
