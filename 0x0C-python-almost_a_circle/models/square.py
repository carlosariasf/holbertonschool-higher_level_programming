#!/usr/bin/python3
"""Esto es un comentario"""


from .rectangle import Rectangle


class Square(Rectangle):
    """Esto es un comentario"""

    def __init__(self, size, x=0, y=0, id=None):
        """Esto es un comentario"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Esto es un comentario"""
        return self.width

    @size.setter
    def size(self, value):
        """Esto es un comentario"""
        self.valdata("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Esto es un comentario"""
        if args:
            la = len(args)
            if la >= 1:
                self.id = args[0]
                if la >= 2:
                    self.width = args[1]
                    self.height = args[1]
                    if la >= 3:
                        self.x = args[2]
                        if la > 3 and la < 5:
                            self.y = args[3]
        else:
            if kwargs:
                for att, value in kwargs.items():
                    if att is "id":
                        self.id = value
                    if att is "size":
                        self.width = value
                        self.height = value
                    if att is "x":
                        self.x = value
                    if att is "y":
                        self.y = value

    def to_dictionary(self):
        """Esto es un comentario"""
        dic = {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y,
            }
        return dic

    def __str__(self):
        """Esto es un comentario"""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))
