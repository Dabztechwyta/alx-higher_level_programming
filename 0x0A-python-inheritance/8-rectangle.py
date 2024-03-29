#!/usr/bin/python3
""" class Instantiating """

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
      defines a rectangle-child class of BaseGeometry-parent class
    """
    def __init__(self, width, height):
        ''' defines the init parameters of the Rectangle class '''
        super().integer_validator("width", width)
        super().integer_validator("heigth", height)
        self.__width = width
        self.__height = height
