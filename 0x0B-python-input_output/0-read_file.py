#!/usr/bin/python3
"""Reading files"""


def def read_file(filename=""):
    """Reads file"""

    Args:
        filename(str) -> name
    Returns:
        None

    if filename:
        with open(filename, encoding="utf-8") as f:
            print(f.read(), end="")
