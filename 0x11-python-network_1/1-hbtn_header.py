#!/usr/bin/python3

"""Python script that fetches https://alx-intranet.hbtn.io/status"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.headers
        print(headers.get('X-Request-Id'))
