#!/usr/bin/python3

"""
script  fetches https://alx-intranet.hbtn.io/status
"""

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

url = 'https://alx-intranet.hbtn.io/status'
req = Request(url)
with urlopen(req) as response:
    the_page = response.read()
