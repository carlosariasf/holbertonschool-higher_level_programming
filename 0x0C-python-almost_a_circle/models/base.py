#!/usr/bin/python3
""" """


import json


class Base():
    """ """
    __nb_objects = 0

    def __init__(self, id=None):
        """ """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    def from_json_string(json_string):
        """ """
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """ """
        clsd = cls(1, 1)
        clsd.update(**dictionary)
        return clsd

    @classmethod
    def load_from_file(cls):
        """ """
        ilist = []
        with open("{}.json".format(
                cls.__name__), mode="r", encoding="utf-8") as f:
            if f:
                ilist = f
                print(ilist)
        return ilist

    @classmethod
    def save_to_file(cls, list_objs):
        """ """
        dict2 = []
        with open("{}.json".format(
                cls.__name__), mode="w", encoding="utf-8") as f:
            if list_objs:
                for i in range(len(list_objs)):
                    dict2.append(dict(list_objs[i].to_dictionary()))
                f.write(cls.to_json_string(dict2))
            else:
                f.write("[]")
