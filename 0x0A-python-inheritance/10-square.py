#!/usr/bin/python3
""" class Instantiating """
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
      defines a rectangle-child class of BaseGeometry-parent class
    """
    def __init__(self, size):
        ''' defines the init param of the Rectangle class '''
        super().integer_validator("size", size)
        self.__size = size

    def __str__(self):
        __get = (self.__class__.__name__)
        return ("[{}] {}/{}".format(__get, self.__size, self.__size))

    def area(self):
        return (self.__size ** 2)
