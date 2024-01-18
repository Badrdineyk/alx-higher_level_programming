#!/usr/bin/python3
import sys

if __name__ == "__main__":
    from sys import argv
    from helper import add, sub, mul, div

    arg_len = len(argv) - 1

    if arg_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    operator = argv[2]

    if operator not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(argv[1])
    b = int(argv[3])

    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[operator](a, b)))
