#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    for module in dir(hidden_4):
        if module[:2] != '__':
            print(module)
