#!/usr/bin/python3
"""Module of Square object"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defines a square class"""

    def __init__(self, size):
        """Initializes square parameters"""
        self.integer_validator("width", size)
        self.__size = size

    def area(self):
        """Returns the area of a square"""
        return self.__size * self.__size

    def __str__(self):
        """returns a string representation of square object"""
        return "[Square] {}/{}".format(self.__size, self.__size)
