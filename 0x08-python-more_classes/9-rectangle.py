#!/usr/bin/python3
class Rectangle:
    """A class storing attributes and methods of a rectangle
        Attributes:
            width(int): private instance attr with property
            height(int): private instace attr with property
            number_of_instances: records number of objects made
            print_symbol(any type): public class symbol used to print rectangle
        Methods:
            area: public instance, returns area
            perimeter: public instance, returns perimeter
            __del__: displays a messge before deleting an object
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes private instace width and height"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width to args value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of rectangle (width * height)"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns perimeter of rectangle"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ sting repr of rectangle
        Prints # in the shape of rectangle's width and height
        """
        return (Rectangle.print_symbol * self.__width + "\n") * self.__height

    def __repr__(self):
        """ official representation of rectangle object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """deletes an instance of rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """ class method, returns a square object"""
        return cls(size, size)
