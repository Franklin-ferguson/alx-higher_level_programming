#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays
"""
from urllib.request import Request, urlopen
from sys import argv
from urllib.error import HTTPError, URLError


if __name__ == "__main__":

    url = argv[1]

    req = Request(url)
    try:
        with urlopen(req) as response:
            print(response.read().decode("ascii"))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
