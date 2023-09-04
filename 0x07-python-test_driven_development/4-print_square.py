#!/usr/bin/python3
""" Module prints a square using #
"""


def print_square(size):
    """ prints a square figure using the sign #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(((size * "#") + "\n") * size, end="")
