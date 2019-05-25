#!/usr/bin/python3
"""Python Module

    Functions:
        say_my_name
"""
def say_my_name(first_name, last_name=""):
    """Function to print a first name and last name

    Args:
        first_name: String with name
        last_name: String with last name
    """
    try:
        try:
            if type(first_name) is str:
                pass
            else:
                raise TypeError
        except TypeError as e:
            raise Exception("first_name must be a string") from e
        try:
            if type(last_name) is str:
                pass
            else:
                raise TypeError
        except TypeError as e:
            raise Exception("last_name must be a string") from e
    except Exception as err:
        print(err)
        return
    print("My name is {} {}".format(first_name, last_name))
