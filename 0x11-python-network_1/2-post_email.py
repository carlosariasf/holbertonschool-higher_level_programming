#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
import urllib.request
import sys


if __name__ == "__main__":
    """Python script that fetches https://intranet.hbtn.io/status"""
    data = urllib.parse.urlencode({'email': '{}'.format(sys.argv[2])})
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode("UTF-8"))
