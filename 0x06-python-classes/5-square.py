#!/usr/bin/python3
"""class"""


class Square:
    """square"""

    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self._Square__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")
        self._Square__size = value

    def area(self):
        """Return the current square area"""
        return self._Square__size * self._Square__size

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
        pass
