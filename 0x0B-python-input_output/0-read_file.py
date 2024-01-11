#!/usr/bin/python3
''' Initializing Module '''

def read_file(filename=""):
    '''
      Reads a text file(UT8) and prints it to stdout
    '''
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
