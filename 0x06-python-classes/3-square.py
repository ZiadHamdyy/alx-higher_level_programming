#!/usr/bin/python3
"""class"""


class Square:
    """square"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self._Square__size = size

    def area(self):
        """Return the current square area"""
        return self._Square__size * self._Square__size
        pass
