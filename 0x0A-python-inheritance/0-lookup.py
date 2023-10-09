#!/usr/bin/python3
"""lookup"""


def lookup(obj):
    """lookup"""

    attributes_and_methods = dir(obj)
    filtered_attributes_and_methods = [item for item in attributes_and_methods if not item.startswith("__")]
    return filtered_attributes_and_methods
