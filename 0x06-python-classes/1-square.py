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
        self.__size = size
