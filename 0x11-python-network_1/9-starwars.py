#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
import requests
import sys


if __name__ == "__main__":
    """Python script that fetches https://intranet.hbtn.io/status"""
    url = "https://swapi.co/api/people/"
    if len(sys.argv) < 2:
        q = '?search='
    else:
        q = '?search={}'.format(sys.argv[1])
    r = requests.get(url + q)
    try:
        req = r.json()
        if req == {}:
            print("No result")
        else:
            print("Number of results: {}".format(req.get("count")))
            for i in range(len(req["results"])):
                result = req["results"][i]
                print("{}".format(result.get("name")))
    except:
        print("Not a valid JSON")
