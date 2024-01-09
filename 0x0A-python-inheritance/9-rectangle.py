#!/usr/bin/python3
""" class Instantiating """

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
      defines a rectangle-child class of BaseGeometry-parent class
    """
    def __init__(self, width, height):
        ''' defines the init param of the Rectangle class '''
        super().integer_validator("width", width)
        super().integer_validator("heigth", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        __get = (self.__class__.__name__)
        return ("[{}] {}/{}".format(__get, self.__width, self.__height))

    def area(self):
        return (self.__width * self.__height)
