#!/usr/bin/python3

""" Module 1-write_file.py """

from sys import argv
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

items += argv[1:]

save_to_json_file(items, filename)
