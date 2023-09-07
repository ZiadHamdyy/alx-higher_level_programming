#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    arguments = sys.argv
    number = len(arguments)
    if number == 1:
        print("{} argument:".format(number - 1))
    else:
        print("{} arguments:".format(number - 1))

    for i in range(1, number):
        print("{}: {}".format(i, arguments[i]))
