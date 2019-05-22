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
