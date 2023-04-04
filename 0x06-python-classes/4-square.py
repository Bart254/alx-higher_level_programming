#!/usr/bin/python3
"""This is an introduction to OOP
    Module creates a Square class
"""


class Square:
    """Defines the building blocks of a square
    Attributes:
        size(int): private instance
        area: public insatnce method
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

    def area(self):
        """Has no parameters
            Returns the area of square based on size
        """
        return self.__size * self.__size

    @property
    def size(self):
        """retrieves size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """uses value to change the size of square
        """
        self.__init__(value)
