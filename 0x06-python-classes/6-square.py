#!/usr/bin/python3
"""This is an introduction to OOP
    Module creates a Square class
"""


class Square:
    """Defines the building blocks of a square
    Attributes:
        size(int): private instance
        area: public insatnce method
        size(int): setter for size
        size: getter for size
        my_print: public class method
    """
    def __init__(self, size=0, position=(0, 0)):
        """defines a private instance attribute size
        Args:
            size(int): length/width of square
            position(tuple): tuple of two positive integers
            """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
        if type(value) is not int:
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__size = value

    def my_print(self):
        """prints the area of square using #
        """
        nb = self.__size
        while nb:
            if self.__position[1] <= self.__position[0]:
                for i in range(self.__position[0]):
                    print(" ", end="")
            for i in range(self.__size):
                print("#", end="")
            print()
            nb -= 1
        if self.__size == 0:
            print()

    @property
    def position(self):
        """Returns the position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position of square
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("value must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("value must be a tuple of 2 positive integers")
        self.__position = value
