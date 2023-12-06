#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list = []
    for e in my_list:
        list.append(e % 2 == 0)

    return list
