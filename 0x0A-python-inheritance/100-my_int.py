#!/usr/bin/python3
""" Instantiate Module """

class MyInt(int):
    """ defines a function that reverses the comparison operators """
    def __init__(self, value):
        """ take an initial value """
        self.__value = value

    def __eq__(self, value):
        """
          take value not equal to itself
        """
        return (self.__value != value)

    def __ne__(self, value):
        return (self.__value == value)
