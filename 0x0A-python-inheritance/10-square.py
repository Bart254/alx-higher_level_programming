#!/usr/bin/python3
"""creates a square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """initialization of sides of the square"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """computes area of a square"""
        return self.__size ** 2
