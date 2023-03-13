#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)
    if length == 0:
        return ''
    if length == 1:
        if my_string[0] == 'c' or my_string[0] == 'C':
            return ''
        return my_string[0]
    elif my_string[0] == 'c' or my_string[0] == 'C':
        return '' + no_c(my_string[1:])
    return my_string[0] + no_c(my_string[1:])
