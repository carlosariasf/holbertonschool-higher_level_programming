#!/usr/bin/python3
"""Esto es un comentario"""


from .base import Base


class Rectangle(Base):
    """Esto es un comentario"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Esto es un comentario"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Esto es un comentario"""
        return self.__width

    @width.setter
    def width(self, value):
        """Esto es un comentario"""
        self.valdata("width", value)
        self.__width = value

    @property
    def height(self):
        """Esto es un comentario"""
        return self.__height

    @height.setter
    def height(self, value):
        """Esto es un comentario"""
        self.valdata("height", value)
        self.__height = value

    @property
    def x(self):
        """Esto es un comentario"""
        return self.__x

    @x.setter
    def x(self, value):
        """Esto es un comentario"""
        self.valdata("x", value)
        self.__x = value

    @property
    def y(self):
        """Esto es un comentario"""
        return self.__y

    @y.setter
    def y(self, value):
        """Esto es un comentario"""
        self.valdata("y", value)
        self.__y = value

    def area(self):
        """Esto es un comentario"""
        return self.__width * self.__height

    def display(self):
        """Esto es un comentario"""
        print(("{}").format('\n' * self.__y), end='')
        for i in range(self.__height):
            print("{}".format(' ' * self.__x), end='')
            print("{}".format('#' * self.__width), end='')
            print('')

    def update(self, *args, **kwargs):
        """Esto es un comentario"""
        if args and type(args) is int:
            la = len(args)
            if la >= 1:
                self.id = args[0]
                if la >= 2:
                    self.width = args[1]
                    if la >= 3:
                        self.height = args[2]
                        if la >= 4:
                            self.x = args[3]
                            if la >=5:
                                self.y = args[4]
        else:
            if kwargs:
                for att, value in kwargs.items():
                    if att is "id":
                        self.id = value
                    if att is "width":
                        self.width = value
                    if att is "height":
                        self.height = value
                    if att is "x":
                        self.x = value
                    if att is "y":
                        self.y = value

    def __str__(self):
        """Esto es un comentario"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def to_dictionary(self):
        """Esto es un comentario"""
        dic = {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y,
            }
        return dic

    def valdata(self, name, value):
        """Esto es un comentario"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
            return
        if name is 'x' or name is 'y':
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
                return
        if name is "width" or name is "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
                return
