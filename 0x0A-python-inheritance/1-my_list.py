#!/usr/bin/python3
""" Module to Initialize """

class MyList(list):
    """ class inherits the object 'list' """
    def print_sorted(self):
        """ Function prints a sorted list 
            in ascending order
        """
        print(sorted(self))
