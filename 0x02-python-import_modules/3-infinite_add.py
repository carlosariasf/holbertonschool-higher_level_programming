#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    count = 0
    if len(argv) == 1:
        print("{}".format(0))
    else:
        for i in range(1, len(argv)):
            count += int(argv[i])
        print("{}".format(int(count)))
