#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        my_list.sort(reverse=True)
        for e in my_list:
            print("{:d}".format(e))
