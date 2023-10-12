#!/usr/bin/python3

def number_keys(a_dictionary):
    count = 0
    thekeys = list(a_dictionary.keys())

    for i in thekeys:
        count += 1

    return count
