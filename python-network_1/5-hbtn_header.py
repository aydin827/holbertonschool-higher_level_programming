#!/usr/bin/python3
import requests
import sys
url = sys.argv[1]
response = requests.get(url)
print(content.headers.get("X-Request-Id"))
