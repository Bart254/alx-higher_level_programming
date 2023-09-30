#!/usr/bin/python3
"""script adds all arguments to a Python list, and then save them to a file
"""
import sys
import json


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
try:
    exist_d = load_from_json_file("add_item.json")
except FileNotFoundError:
    exist_d = []
for arg in sys.argv[1:]:
    exist_d.append(arg)

save_to_json_file(exist_d, "add_item.json")
