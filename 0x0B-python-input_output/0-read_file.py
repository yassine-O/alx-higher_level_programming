#!/usr/bin/python3

""" Module 0-read_file.py """


def read_file(filename=""):
    """ 0-read_file documentation """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
