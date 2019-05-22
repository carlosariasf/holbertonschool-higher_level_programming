#!/usr/bin/python3
class Node():
    '''A class of Node

    Attributes:
        data: data
        next_node: node
    '''
    def __init__(self, data, next_node=None):
        """Inits Node with data and nextnode, only allowed type int > 0."""
        try:
            try:
                if type(data) == int:
                    self.__data = data
            except TypeError as e:
                raise Exception("data must be an integer") from e
            try:
                if type(next_node) == Node:
                    self._data = next_node
            except TypeError as e:
                raise Exception("next_node must be a Node object") from e
        except Exception as err:
            print(err)
