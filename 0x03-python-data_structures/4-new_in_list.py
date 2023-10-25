#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = len(my_list)

    new = my_list[:]

    if 0 <= idx < n:
        new[idx] = element

    return (new)
