#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
import urllib.request
import sys


if __name__ == "__main__":
    """Python script that fetches https://intranet.hbtn.io/status"""
    try:
        with urllib.request.urlopen(
                '{}'.format(sys.argv[1])) as response:
            print(response.read().decode("UTF-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
