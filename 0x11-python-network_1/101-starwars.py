#!/usr/bin/python3
"""Python script that fetches from swapi"""
import requests
import sys


if __name__ == "__main__":
    """Python script that fetches form swapi"""
    url = "https://swapi.co/api/people/"
    q = {'search': sys.argv[1]}
    r = requests.get(url, params=q)
    cn = r.json()
    print("Number of results: {}".format(cn.get("count")))
    result = r.json().get("results")
    i = 0
    while i < len(result):
        print(result[i].get("name"))
        i += 1
        if i == len(result) and cn.get("next") is not None:
            r = requests.get(cn.get("next"))
            result = r.json().get("results")
            cn = r.json()
            i = 0
