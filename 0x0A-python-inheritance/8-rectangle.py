#!/usr/bin/python3
""" """


BG = __import__('7-base_geometry').BaseGeometry


class Rectangle(BG):
    """ """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self__width = width
        self__height = height
