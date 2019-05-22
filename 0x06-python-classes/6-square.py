#!/usr/bin/python3
class Square():
    """A class used to represent a square.

    Attributes:
        __size: A private int with size of Square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Inits Square with size, pnly allowed type int > 0."""
        try:
            try:
                if not type(size) == int:
                    raise TypeError
            except TypeError as e:
                raise Exception("size must be an integer") from e
            try:
                if (int(size) < 0):
                    raise ValueError
                self.__size = size
            except ValueError as e:
                raise Exception("size must be >= 0") from e
            try:
                check = 0
                if type(position) is tuple:
                    if len(position) == 2:
                        for i in position:
                            if type(i) == int:
                                if i >= 0:
                                    check += 1
                if check != 2:
                    raise TypeError
                self.__position = position
            except TypeError as e:
                raise Exception("position must be a tuple "
                                "of 2 positive integers") from e
        except Exception as err:
            print(err)

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
            try:
                if not type(size) == int:
                    raise TypeError
            except TypeError as e:
                raise Exception("size must be an integer") from e
            try:
                if (int(value) < 0):
                    raise ValueError
                self.__size = value
            except ValueError as e:
                raise Exception("size must be >= 0") from e
        except Exception as err:
            print(err)

    @property
    def position(self):
        """Return the size of square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Change the value of size

        Args:
            value: New size
        """
        try:
            try:
                check = 0
                if type(value) is tuple:
                    if len(value) == 2:
                        for i in value:
                            if type(i) == int:
                                if i >= 0:
                                    check += 1
                if check != 2:
                    raise TypeError
                self.__position = value
            except TypeError as e:
                raise Exception("position must be a tuple "
                                "of 2 positive integers") from e
        except Exception as err:
            print(err)

    def area(self):
        """Returns the area of square."""
        return self.__size * self.__size

    def my_print(self):
        """Print square"""
        if self.__size == 0:
            print("")
        else:
            print('\n' * (int(self.__position[1])), end='')
            for i in range(self.__size):
                print(" " * (int(self.__position[0])), end='')
                for j in range(self.__size):
                    print("#", end='')
                print("")
