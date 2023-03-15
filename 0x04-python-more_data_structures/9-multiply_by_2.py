#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        square_values = list(map(lambda a: a * a, a_dictionary.values()))
        new_dict = {}
        element = 0
        for key in a_dictionary:
            new_dict.update({key: square_values[element]})
            element += 1
        return new_dict
