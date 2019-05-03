#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    count = 1
    if len(argv) == 1:
        print("{} arguments.".format(0))
    for i in range(1, len(argv)):
        if len(argv) == 2:
            print("{} argument:\n{}: {}".format(1, 1, argv[1]))
        if len(argv) != 2:
            if count == 1:
                print("{} arguments:".format(len(argv) - 1))
                count += 1
            print("{}: {}".format(i, argv[i]))
