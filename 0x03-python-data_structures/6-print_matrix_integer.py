#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for member in matrix:
        length = len(member)
        last_index = length - 1
        for e in range(length):
            if e == last_index:
                print("{:d}".format(member[e]), end='')
            else:
                print("{:d}".format(member[e]), end=' ')
        print()
