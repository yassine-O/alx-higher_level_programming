#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)

    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    f = {'+': add, '-': sub, '*': mul, '/': div}

    if op not in f:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    res = f[op](a, b)
    print(f"{a} {op} {b} = {res}")
