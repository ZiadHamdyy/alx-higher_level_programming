#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = list(set(my_list))
    result = 0
    for i in range(0, len(my_set)):
        result += my_set[i]
    return result
