#!/usr/bin/python3
"""get commits"""
import requests
from sys import argv


if __name__ == "__main__":
    """Get commits from github"""
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    r = requests.get(url)
    req = r.json()
    for i in range(10):
        print("{}: ".format(req[i].get('sha')), end="")
        commit = req[i].get("commit")
        auth = commit.get("author")
        print("{}".format(auth.get("name")))
