#!/usr/bin/python3

def lookup(obj):
    """lookup"""

    attributes = dir(obj)
    for i in attributes:
        if not i.startswith("__"):
            return attributes
