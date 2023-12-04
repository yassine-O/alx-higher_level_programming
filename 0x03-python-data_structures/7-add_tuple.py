#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    list = [0, 0]
    for i in range(2):
        list[i] += tuple_a[i] if len(tuple_a) > i else 0
        list[i] += tuple_b[i] if len(tuple_b) > i else 0

    return tuple(list)
