#!/usr/bin/python3

def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers """
    n = len(list_of_integers)
    if n == 0:
        return None
    peak = list_of_integers.sort()
    return list_of_integers[-1]

