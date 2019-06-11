#!/usr/bin/python3
"""Esto es un comentario"""


import json


class Base():
    """Esto es un comentario"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Esto es un comentario"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Esto es un comentario"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @staticmethod
    def from_json_string(json_string):
        """Esto es un comentario"""
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Esto es un comentario"""
        clsd = cls(1, 1)
        clsd.update(**dictionary)
        return clsd

    @classmethod
    def load_from_file(cls):
        """Esto es un comentario"""
        ilist = []
        with open("{}.json".format(
                cls.__name__), mode="r", encoding="utf-8") as f:
            if f:
                ilist = f
                print(ilist)
        return ilist

    @classmethod
    def save_to_file(cls, list_objs):
        """Esto es un comentario"""
        dict2 = []
        with open("{}.json".format(
                cls.__name__), mode="w", encoding="utf-8") as f:
            if list_objs:
                for i in range(len(list_objs)):
                    dict2.append(dict(list_objs[i].to_dictionary()))
                f.write(cls.to_json_string(dict2))
            else:
                f.write("[]")
