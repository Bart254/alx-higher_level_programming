#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb_printed = 0
    try:
        for e in range(x):
            print(my_list[e], end="")
            nb_printed += 1
    except IndexError:
        pass
    print()
    return nb_printed
