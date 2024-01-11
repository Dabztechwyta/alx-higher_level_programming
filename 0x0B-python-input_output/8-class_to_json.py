#!/usr/bin/python3
''' Initializing Module '''

def class_to_json(obj):
    '''
      Returns the dictionary description with simple data structure
      for Json serialization of an object
    '''
    return(obj.__dict__)
