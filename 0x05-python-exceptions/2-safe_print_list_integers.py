#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb_printed = 0
    try:
        for e in range(x):
            if type(my_list[e]) is int:
                print("{:d}".format(my_list[e]), end="")
                nb_printed += 1
    except IndexError:
        raise
    print()
    return nb_printed
