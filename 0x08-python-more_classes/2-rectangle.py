#!/usr/bin/python3
"""
   Define a class Rectangle
"""

class Rectangle:
    """ initializing the class Rectangle """

    def __init__(self, width=0, height=0):
        """ Inital Parameters """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ property getter """

        return self.__width

    @width.setter
    def width(self, value):
        """ Property setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ property getter """

        return self.height

    @height.setter
    def height(self, value):
        """property setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value 

    def area(self):
        """ solves for area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ solves for perimeter of rect """
        return 2 * (self.__width + self.__height)
