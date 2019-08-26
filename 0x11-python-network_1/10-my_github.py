#!/usr/bin/python3
"""Python script that fetches from swapi"""
import requests
import sys


if __name__ == "__main__":
    """Python script that fetches form swapi"""
    url = "https://api.github.com/user"
    q = (sys.argv[1], sys.argv[2])
    r = requests.get(url, auth=q)
    print(r.json().get("id"))
