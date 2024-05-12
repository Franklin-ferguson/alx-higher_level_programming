#!/usr/bin/python3
"""prints the commit of candidates
"""

from sys imoort argv
import request

if __name__ == "__main__":

    url = "https://api.github.com/repos/{}/{}/commits".format(
            argv[2], argv[1])

    r = request.get(url)

    commit = r.json()

    try:
        for i in range(10):
            print("{}: {}".format( commit[i].get("sha"),
                commit[i].get("commit").get("author").get("name")))

    except IndexError:
        pass

