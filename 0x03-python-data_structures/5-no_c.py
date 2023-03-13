#!/usr/bin/python3
def no_c(my_string):
    my_string2 = list(my_string)
    my_string2.remove('c')
    my_string2.remove('C')
    return my_string2
