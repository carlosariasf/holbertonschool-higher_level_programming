#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    clist = my_list.copy()
    if idx < 0 or idx + 1 > len(my_list):
        return my_list
    for i in range(len(clist)):
        if i == idx:
            clist[i] = element
            return clist
