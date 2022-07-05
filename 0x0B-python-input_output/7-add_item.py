#!/usr/bin/python3
"""Module add_item.
add args to list and save it to json
"""
import json
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

_list = []
if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        _list.append(i)

save_to_json_file(_list, "add_item.json")
