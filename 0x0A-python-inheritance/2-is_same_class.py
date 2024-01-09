#!/usr/bin/python3
""" Module Initializing """

def is_same_class(obj, a_class):
    """
      A function that checks if object is an exact instance
      of the specified class and then returns True or False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
