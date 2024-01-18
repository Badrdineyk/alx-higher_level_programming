#!/usr/bin/python3
import sys

if __name__ == "__main__":
    from sys import argv
    from helper import add, sub, mul, div

    arg_len = len(argv) - 1

    if arg_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operators = ['+', '-', '*', '/']
    operator = argv[2]

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if operator == '+':
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, add(a, b)))
    if operator == '-':
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, sub(a, b)))
    if operator == '*':
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, mul(a, b)))
    if operator == '/':
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, div(a, b)))
