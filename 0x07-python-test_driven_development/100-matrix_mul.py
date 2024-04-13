#!/usr/bin/python3
"""Matrix multiplication
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices

    Parameters
    -----------
    m_a: list
        First matrix, must be list of list of integers/floats
    m_b: list
        Second matrix, must be a list of int/float

    Returns
    -------
    list
        a product matrix from m_a * m_b
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    for a_list in m_a:
        if type(a_list) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(a_list) == 0:
            raise ValueError("m_a can't be empty")
        for a_num in a_list:
            if type(a_num) is not int and type(a_num) is not float:
                raise TypeError("m_a should contain only integers or floats")
            if len(a_list) != len(m_a[0]):
                raise TypeError("each row of m_a must be of the same size")

    for a_list in m_b:
        if type(a_list) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(a_list) == 0:
            raise ValueError("m_b can't be empty")
        for a_num in a_list:
            if type(a_num) is not int and type(a_num) is not float:
                raise TypeError("m_b should contain only integers or floats")
            if len(a_list) != len(m_b[0]):
                raise TypeError("each row of m_b must be of the same size")

    # check if matrices can be multiplied
    col_a = len(m_a[0])
    col_b = len(m_b[0])
    row_b = len(m_b)
    if col_a != row_b:
        raise ValueError("m_a and m_b can't be multiplied")

    # multiply the matrices
    new_matrix = []
    for row in m_a:
        new_row = []
        for col in range(col_b):
            product = 0
            i = 0
            while i < col_a:
                product += row[i] * m_b[i][col]
                i += 1
            new_row.append(product)
        new_matrix.append(new_row)
    return new_matrix
