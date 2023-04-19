#!/usr/bin/python3
""" Module creates a division function
"""


def matrix_divided(matrix, div):
    """
    Function divides a matrix list by div and returns results in 2 d.p
    """
    err_msg_1 = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(err_msg_1)
    for e in matrix:
        if type(e) is not list:
            raise TypeError(err_msg_1)
        for i in e:
            if not isinstance(i, (int, float)):
                raise TypeError(err_msg_1)
    mtrx_len = len(matrix[0])
    for my_list in matrix:
        if len(my_list) != mtrx_len:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    div_matrix = []
    div_list = []
    for e in matrix:
        for i in e:
            div_list.append(div)
        div_matrix.append(list(map(lambda a, b: round(a / b, 2), e, div_list)))
    return div_matrix
