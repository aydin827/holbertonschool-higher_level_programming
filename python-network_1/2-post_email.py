#!/usr/bin/python3
"""
s
"""
import urllib.request
import sys
import urllib.parse
url = sys.argv[1]
email = sys.argv[2]
data = urllib.parse.urlencode({'email' : email})
data = data.encode('ascii')
with urllib.request.urlopen(url, data) as response:
    body = response.read()
print(body.decode("utf-8"))
