#!/usr/bin/python3

def remove_char_at(str, n):
    str1 = ""
    i = 0
    for char in str:
        if i != n:
            str1 += char
        i += 1
    return str1
