#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
import urllib.request
import sys


if __name__ == "__main__":
    """Python script that fetches https://intranet.hbtn.io/status"""
    with urllib.request.urlopen(
            '{}'.format(sys.argv[1])) as response:
        print(response.headers.get("X-Request-Id"))
