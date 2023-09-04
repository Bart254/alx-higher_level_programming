#!/usr/bin/python3
""" Module with a matix dividing function
"""


def matrix_divided(matrix, div):
    """ Returns the value after dividing matrix with div
    """
    type_err = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(type_err)
    for e in range(len(matrix)):
        if type(matrix[e]) is not list:
            raise TypeError(type_err)
        for index in matrix[e]:
            if type(index) is not int and type(index) is not float:
                raise TypeError(type_err)
        if len(matrix[0]) != len(matrix[e]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = []
    for element in matrix:
        result.append(list(map(lambda x: round(x/div, 2), element)))
    return result
