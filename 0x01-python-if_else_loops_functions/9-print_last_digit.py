#!/usr/bin/python3

def print_last_digit(number):
    if number >= 0:
        lastdig = number % 10
    else:
        num = number * -1
        lastdig = num % 10
    print("{:d}".format(lastdig), end="")
    return lastdig
