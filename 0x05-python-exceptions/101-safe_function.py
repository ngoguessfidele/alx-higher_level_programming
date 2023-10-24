#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        ret = fct(*args)
    except Exception as n:
        sys.stderr.write("Exception: {}\n".format(n))
        ret = None

    return (ret)
