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

    def area(self):
        """ """
        return self.__width * self.__height

    def perimeter(self):
        """ """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ """
        str_prt = ''
        if self.__width == 0 or self.__height == 0:
            return str_prt
        else:
            for i in range(self.__height):
                str_prt += ('#' * self.__width)
                if i != self.__height - 1:
                    str_prt += '\n'
            return str_prt

    def __repr__(self):
        """ """
        repr_prt = "{self.__class__.__name__} \
            ({self.width}, {self.height})".format(self=self)
        return repr_prt

    def check(self, name, value):
        """ """
        if type(value) == int:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
                return 0
            else:
                return value
        else:
            raise TypeError("{} must be an integer".format(name))
            return 0
