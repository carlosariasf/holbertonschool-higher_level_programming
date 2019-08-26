#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
import requests
import sys


if __name__ == "__main__":
    """Python script that fetches https://intranet.hbtn.io/status"""
    r = requests.get('{}'.format(sys.argv[1]))
    print(r.headers.get("X-Request-Id"))
