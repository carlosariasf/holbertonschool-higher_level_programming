#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    m_list = my_list[::-1]
    for i in range(len(m_list)):
        print("{}".format(m_list[i]))
