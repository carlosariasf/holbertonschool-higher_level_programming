#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
import requests
import sys


if __name__ == "__main__":
    """Python script that fetches https://intranet.hbtn.io/status"""
    url = "http://34.206.234.184:47057/search_user"
    if len(sys.argv) < 2:
        q = ""
    else:
        q = '{}'.format(sys.argv[1])
    r = requests.post(url, data={'q': q})
    if r.json:
        req = r.json()
        if not any(req.values()):
            print("No result")
        else:
            print("[{}] {}".format(req.get("id"), req.get("name")))
    else:
        print("Not a valid JSON")
