#!/usr/bin/python3
""" Class """


class LockedClass():
    """ No attributes unsess first_name """
    __slots__ = ['first_name']

    def __init__(self):
        """ method"""
        pass
