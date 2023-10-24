#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        qot = a / b
    except (TypeError, ZeroDivisionError):
        qot = None
    finally:
        print("Inside result: {}".format(qot))
    return (qot)
