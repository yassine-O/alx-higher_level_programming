#!/usr/bin/python3

for i in range(26):
    if i % 2 == 0:
        print("{:c}".format(ord('z') - i), end='')
    else:
        print("{:c}".format(ord('z') - i - 32), end='')
