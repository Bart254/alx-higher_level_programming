#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        if key in a_dictionary.keys():
            a_dictionary[key] = value
        else:
            a_dictionary.update({key: value})
        return a_dictionary
