#!/usr/bin/python3
"""Python Module

    Functions:
        text_indentation(text)
"""
def text_indentation(text):
    """Function to print a text with some parameters

    Args:
        text: Text to format
    """
    try:
        try:
            if type(text) is str:
                for i in range(len(text)):
                    if str(text)[i] in {".", "?", ":"} and str(text)[i+1] == " ":
                        print(text[i])
                        continue
                    if str(text)[i] == " " and str(text)[i-1] in {".", "?", ":"}:
                        print("")
                    else:
                        print(text[i], end='')
            else:
                raise TypeError
        except TypeError as e:
            raise Exception("text must be a string") from e
    except Exception as err:
        print(err)
