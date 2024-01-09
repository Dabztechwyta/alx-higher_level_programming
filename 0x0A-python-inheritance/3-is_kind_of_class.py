#!/usr/bin/python3
""" Module Initalizing """

def is_kind_of_class(obj, a_class):
    """ 
      A function that checks if the object is an instance of,
      or if the object is an instance of the a class that inherited from,
      the specified class and then return True or False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
