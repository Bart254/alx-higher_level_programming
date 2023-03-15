#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is not None:
        my_set = set(my_list)
        total = 0
        for e in my_set:
            total += e
        return total
