#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        keys_list = list(a_dictionary.keys())
        best_key = keys_list[0]
        best_score = a_dictionary[best_key]
        for key in keys_list:
            if a_dictionary[key] > best_score:
                best_key = key
                best_score = a_dictionary[best_key]
        return best_key
