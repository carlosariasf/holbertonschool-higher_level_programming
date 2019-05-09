#!/usr/bin/python3
def search_replace(my_list, search, replace):
    mylist = list()
    for i in my_list:
        if i == search:
            mylist.append(replace)
        else:
            mylist.append(i)
    return mylist
