#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    len1 = len(my_list)

    if idx < 0 or idx > len1 - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
