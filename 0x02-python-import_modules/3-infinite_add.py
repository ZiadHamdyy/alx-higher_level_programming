#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    argument = sys.argv
    add = 0
    for i in range(1, len(argument)):
        add += int(argument[i])
    print("{:d}".format(add))
