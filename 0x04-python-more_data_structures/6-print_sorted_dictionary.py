#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    theorder = list(a_dictionary.keys())
    theorder.sort()

    for i in theorder:
        print("{}: {}".format(i, a_dictionary.get(i)))
