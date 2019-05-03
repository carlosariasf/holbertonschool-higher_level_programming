#!/usr/bin/python3
if __name__ == '__main__':
    import re
    with open('hidden_4.pyc', 'rb') as f:
        count = 1
        read_data = str(f.read())
        read_d = re.findall('x0*:?\w*[_]\w*', read_data)
        for i in read_d:
            for j in i:
                if count > 3:
                    print("{}".format(j), end="")
                count += 1
            print("")
            count = 1
