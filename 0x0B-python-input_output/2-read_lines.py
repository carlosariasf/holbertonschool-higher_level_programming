#!/usr/bin/python3
""" """


def read_lines(filename="", nb_lines=0):
    """ """
    with open(filename, encoding='utf-8') as f:
        if(nb_lines <= 0):
            print(f.read(), end='')
        while nb_lines:
                line = f.readline()
                print(line, end ='')
                nb_lines -= 1
                if not line:
                    break
