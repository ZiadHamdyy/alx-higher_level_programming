#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ""
    for i in range(0, len(str)):
        if i == n:
            continue
        str2 += str[i]
    return str2
