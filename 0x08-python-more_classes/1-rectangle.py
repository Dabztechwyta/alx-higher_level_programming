#!/usr/bin/python3
"""
A class Rectangle
that defines a rectangle
"""
class Rectangle:
    """ Initializing the class Rectangle """
    
    def __init__(self, width=0, height=0):
        """
        Args: Width, Height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Property getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Property setter """
        if type(value) is not int:
            raise TypeError("width must be an int")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ property getter """
        return self.__height
    
    @height.setter
    def height(self, value):
        """ Property setter """
        if type(value) is not int:
             raise TypeError("width must be an int")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value
