#!/usr/bin/python3
class Square():
    """A class used to represent a square.

    Attributes:
        __size: A private int with size of Square.
    """
    def __init__(self, size=0):
        """Inits Square with size, pnly allowed type int > 0."""
        try:
            size + 2
        except TypeError as e:
            raise Exception("size must be an integer") from e
        try:
            if (int(size) < 0):
                raise ValueError
            self.__size = size
        except ValueError as e:
            raise Exception("size must be >= 0") from e

    @property
    def size(self):
        """Return the size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Change the value of size

        Args:
            value: New size
        """
        try:
            value + 2
        except TypeError as e:
            raise Exception("size must be an integer") from e
        try:
            if (int(value) < 0):
                raise ValueError
            self.__size = value
        except ValueError as e:
            raise Exception("size must be >= 0") from e

    def area(self):
        """Returns the area of square."""
        return self.__size * self.__size

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.__size < other.__size

    def __le__(self, other):
        if isinstance(other, Square):
            return self.__size <= other.__size

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.__size == other.__size

    def __ne__(self, other):
        if isinstance(other, Square):
            return self.__size != other.__size

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.__size > other.__size

    def __ge__(self, other):
        if isinstance(other, Square):
            return self.__size >= other.__size
