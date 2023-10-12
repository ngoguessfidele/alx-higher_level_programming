#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    thekeys = list(a_dictionary.keys())

    for i in thekeys:
        if value == a_dictionary.get(i):
            del a_dictionary[i]

    return (a_dictionary)
