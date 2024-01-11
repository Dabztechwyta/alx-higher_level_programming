#!/usr/bin/python3
''' Initializing Module '''

def write_file(filename="", text=""):
    '''
      Writes strings to a text file(UT8) and returns num of
      characters written
    '''
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
