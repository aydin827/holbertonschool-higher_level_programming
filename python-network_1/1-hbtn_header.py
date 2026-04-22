#!/usr/bin/python3
"""
This script takes a URL as an argument, sends a request to the URL,
and displays the value of the X-Request-Id variable found in the header.
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    headers = {'cfclearance': 'true'}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
