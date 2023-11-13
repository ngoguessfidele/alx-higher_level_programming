#!/usr/bin/python3
def add_integer(a, b=98):
    """Adds a and b"""

    try:
        if not(isinstance(a, int)) and not isinstance(a, float):
            raise TypeError("a must be an integer")
        elif not (isinstance(b, int)) and not isinstance(b, float):
            raise TypeError("b must be an integer")
        else:
            if isinstance(a, float) or isinstance(b, float):
                return (int(a) + int(b))
            return a + b
    except Exception as e:
        return (e)
