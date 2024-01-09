#!/usr/bin/python3

""" Module 1-write_file.py """


def append_write(filename="", text=""):
    """ 1-write_file documentation """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
