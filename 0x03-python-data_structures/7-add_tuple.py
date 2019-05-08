#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sumt = ()
    if tuple_a and tuple_a[0]:
        if tuple_b and tuple_b[0]:
            sumt = (tuple_a[0] + tuple_b[0])
        else:
            sumt = (tuple_a[0] + 0)
    else:
        if tuple_b and tuple_b[0]:
            sumt = (tuple_b[0] + 0)
        else:
            sumt = (0 + 0)

    if tuple_a and len(tuple_a) > 1:
        if tuple_b and len(tuple_b) > 1:
            sumt = sumt, (tuple_a[1] + tuple_b[1])
        else:
            sumt = sumt, (tuple_a[1] + 0)
    else:
        if tuple_b and len(tuple_b) > 1:
            sumt = sumt, (tuple_b[1] + 0)
        else:
            sumt = sumt, (0 + 0)
    return sumt
