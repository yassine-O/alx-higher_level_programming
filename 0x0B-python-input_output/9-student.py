#!/usr/bin/python3

"""Module 9-student.py"""


class Student:
    """ 9-student documentation """

    def __init__(self, first_name, last_name, age):
        """ Constructor Method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Serializer method """
        return self.__dict__
