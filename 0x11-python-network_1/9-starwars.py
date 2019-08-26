#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
import requests
import sys


if __name__ == "__main__":
    """Python script that fetches https://intranet.hbtn.io/status"""
    url = "https://swapi.co/api/people/"
    q = {'search': sys.argv[1]}
    r = requests.get(url, params=q)
    cn = r.json().get('count')
    print("Number of results: {}".format(cn))
    result = r.json().get("results")
    for i in range(len(result)):
        print(result[i].get("name"))
