#!/usr/bin/python3
"""get commits"""
import requests
from sys import argv


if __name__ == "__main__":
    """Get commits from github"""
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    r = requests.get(url)
    j = 0
    for i in sorted(r.json(), key=lambda i: i.get.get("commit")
                    .get("author").get("date"), reverse=True):
        print("{}: ".format(req[i].get("sha")), end="")
        print("{}".format(req[i].get("commit").get("author").get("name")))
        j += 1
        if j == 10:
            break
