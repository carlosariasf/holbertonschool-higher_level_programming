#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
import requests
import sys


if __name__ == "__main__":
    """Python script that fetches https://intranet.hbtn.io/status"""
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 2:
        q = ""
    else:
        q = '{}'.format(sys.argv[1])
    r = requests.post(url, data={'q': q})
    try:
        req = r.json()
        if req == {}:
            print("No result")
        else:
            print("[{}] {}".format(req.get("id"), req.get("name")))
    except:
        print("Not a valid JSON")
