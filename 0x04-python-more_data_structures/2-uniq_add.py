#!/usr/bin/python3

def uniq_add(my_list=[]):
    thelist = set(my_list)
    n = 0
    for i in thelist:
        n += i
    return n
