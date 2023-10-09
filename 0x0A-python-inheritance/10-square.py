#!/usr/bin/python3
"""class"""


class BaseGeometry:
    """BaseGeometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area"""

        return self.__width * self.__height

    def __str__(self):
        """str"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square"""

    def __init__(self, size):
        """init"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area"""

        return self.__size ** 2
