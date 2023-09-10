#!/usr/bin/python3
def max_integer(my_list=[]):
    i = 0
    if my_list == []:
        return None
    element = my_list[i]
    for i in range(0, len(my_list)):
        if my_list[i] > element:
            element = my_list[i]
    return element
