#!/usr/bin/python3
"""This is an introduction to OOP
    Module creates a Square class
"""


class Square:
    """Defines the building blocks of a square
    """
    def __init__(self, size=0):
        """defines a private instance attribute size
        Args:
            size(int): length/width of square
            """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
