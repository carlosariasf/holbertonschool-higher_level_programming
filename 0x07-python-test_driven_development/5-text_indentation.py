#!/usr/bin/python3
def text_indentation(text):
    """ Comments  """
    if type(text) is str:
        for i in range(len(text)):
            if str(text)[i] in {".", "?", ":"} and str(text)[i+1] == " ":
                print(text[i])
                continue
            if str(text)[i] == " " and str(text)[i-1] in {".", "?", ":"}:
                print("")
            else:
                print(text[i], end='')
