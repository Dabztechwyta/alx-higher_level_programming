#!/usr/bin/python3
""" Module Initializing """

def inherits_from(obj, a_class):
    """ Inherits an object as an instance of a class,
        returns True or False
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
