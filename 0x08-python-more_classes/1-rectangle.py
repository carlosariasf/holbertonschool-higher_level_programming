#!/usr/bin/python3
class Rectangle():
    """ """
    def __init__(self, width=0, height=0):
        """ """
        self.__width = self.check("width", width)
        self.__height = self.check("height", height)

    @property
    def width(self):
        """ """
        return self.__width

    @width.setter
    def width(self, value):
        """ """
        self.__width = self.check("width", value)

    @property
    def height(self):
        """ """
        return self.__height

    @height.setter
    def height(self, value):
        """ """
        self.__height = self.check("height", value)

    def check(self, name, value):
        """ """
        if type(value) == int:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
                return -1
            else:
                return value
        else:
            raise TypeError("{} must be an integer".format(name))
            return -1
