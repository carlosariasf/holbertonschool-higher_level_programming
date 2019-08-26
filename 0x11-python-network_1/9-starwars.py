#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
import requests
import sys


if __name__ == "__main__":
    """Python script that fetches https://intranet.hbtn.io/status"""
    url = "https://swapi.co/api/people/"
    q = {'search': sys.argv[1]}
    r = requests.get(url, params=q)
    req = r.json()
    print("Number of results: {}".format(req.get("count")))
    for i in range(len(req["results"])):
        result = req["results"][i]
        print("{}".format(result.get("name")))
