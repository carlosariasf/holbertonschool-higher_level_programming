#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
import requests
import sys


if __name__ == "__main__":
    """Python script that fetches https://intranet.hbtn.io/status"""
    r = requests.get('{}'.format(sys.argv[1]))
    code = r.status_code
    if code is 200:
        print(r.text)
    else:
        print("Error code: {}".format(code))
