#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return "None"
    largest = my_list[0]
    for e in range(1, length):
        if largest < my_list[e]:
            largest = my_list[e]
    return largest
