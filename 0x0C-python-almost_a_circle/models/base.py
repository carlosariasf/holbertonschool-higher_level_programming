#!/usr/bin/python3
"""Esto es un comentario"""


import json
import csv


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
        if cls.__name__ is "Rectangle":
            clsd = cls(1, 1)
        else:
            clsd = cls(1)
        clsd.update(**dictionary)
        return clsd

    @classmethod
    def load_from_file(cls):
        """Esto es un comentario"""
        try:
            with open("{}.json".format(
                    cls.__name__), mode="r", encoding="utf-8") as f:
                slist = cls.from_json_string(f.read())
                ilist = []
                for i in slist:
                    ilist.append(cls.create(**i))
                return ilist
        except:
            return []

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

    @classmethod
    def load_from_file_csv(cls):
        """Esto es un comentario"""
        try:
            with open("{}.csv".format(
                    cls.__name__), mode="r", encoding="utf-8") as f:
                slist = csv.DictReader(f)
                ilist = []
                for i in slist:
                    ilist.append(cls.create(**i))
                return ilist
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Esto es un comentario"""
        dic = []
        fieldnames = []
        if cls.__name__ == "Rectangle":
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        else:
            fieldnames = ['id', 'size', 'x', 'y']
        with open("{}.csv".format(
                cls.__name__), mode="w", encoding="utf-8") as f:
            if list_objs:
                for i in list_objs:
                    dic.append(i.to_dictionary())
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for j in dic:
                    writer.writerow(j)
            else:
                f.write("[]")
