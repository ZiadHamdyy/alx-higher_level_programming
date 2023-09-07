#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as calc
    import sys
    arguments = sys.argv
    if len(arguments) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if arguments[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    op = ['+', '-', '*', '/']
    fun = [calc.add, calc.sub, calc.mul, calc.div]
    for i in range(len(op)):
        if arguments[2] == op[i]:
            print("{:d} {} {:d} = {}".format(arguments[1], op[i], arguments[3],
                  fun[i](int(arguments[1]), int(arguments[3]))))
            exit(0)
