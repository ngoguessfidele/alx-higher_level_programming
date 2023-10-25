#!/usr/bin/python3
def no_c(my_string):
    n = len(my_string)

    i = 0

    new = my_string[:]

    for j in range(n):
        if (my_string[j] == 'c' or my_string[j] == 'C'):
            new = new[:(j - i)] + my_string[(j + 1):]
            i += 1

    return (new)
