#!/usr/bin/python3
"""
d
"""
import requests
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    auth = (username, password)
    response = requests.get(url, auth=(username, password))
    data = response.json()
    print(data.get("id"))
