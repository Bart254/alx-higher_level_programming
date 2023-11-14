#!/usr/bin/python3
""" returns the dictionary description with simple data structure
"""


def class_to_json(obj):
    """ returns the dictionary description
    """
    if not hasattr(obj, "__dict__"):
        raise ValueError("The input object must be an instance of a class.")
    serialized_data = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialized_data[key] = value
    return serialized_data
