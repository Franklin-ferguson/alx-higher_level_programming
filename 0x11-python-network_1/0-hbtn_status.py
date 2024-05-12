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
        the_page = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(the_page)))
        print("\t- content: {}".format(the_page))
        print("\t- utf8 content: {}".format(the_page.decode("utf-8")))
