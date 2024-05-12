#!/usr/bin/python3

"""
script  fetches https://alx-intranet.hbtn.io/status
"""

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    req = Request(url)
    with urlopen(req) as response:
        status_code = response.getcode()
        the_page = response.read().decode()
        lines = the_page.splitlines()

        print("{}".format(status_code))
        print("\nBody: ")
        for line in lines:
            print("{}".format(line))
