#!/usr/bin/python3
""" Initializing Module """

class BaseGeometry:
    ''' Defines a class basegeometry '''

    def area(self):
        ''' raises an area exception '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' validates value '''
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (int(value) <= 0):
            raise ValueError("{} must be greater than 0".format(name))

