#!/usr/bin/python3
"""class"""


class Rectangle:
    """Rectangle"""

    def __init__(self, width=0, height=0):
        """__init__"""

        self.wigth = width
        self.height = height

    @property
    def width(self):
        """width"""

        return self.__width

    @width.setter
    def width(self, value):
        """width Erorr"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height"""

        return self.__height

    @height.setter
    def height(self, value):
        """height Erorr"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
