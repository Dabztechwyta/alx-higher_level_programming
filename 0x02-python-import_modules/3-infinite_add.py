#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    args = argv[1:]

    infinite_sum = 0

    if (len(args) > 0):
        for j in range(len(args)):
            infinite_sum += int(args[j])
        print('{:d}'.format(infinite_sum))
