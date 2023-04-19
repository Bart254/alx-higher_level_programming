#!/usr/bin/python3
"""
    Module creates a function that prints a square
"""


def print_square(size):
    """ prints a square using # symbol with size being length of sqaure"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(("#" * size + '\n') * (size - 1) + "#" * size)
