#!/usr/bin/python3
"""
f
"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(content.headers.get("X-Request-Id"))
