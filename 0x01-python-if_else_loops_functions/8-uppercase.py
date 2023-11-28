#!/usr/bin/python3

def uppercase(str):
    for ch in str:
        d = ord(ch)
        if ord('a') <= d <= ord('z'):
            d -= 32
        print("{:c}".format(d), end='')
    print()
