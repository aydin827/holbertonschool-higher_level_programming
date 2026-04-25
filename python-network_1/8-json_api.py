#!/usr/bin/python3
"""
Search API
"""
import requests
import sys

if __name__ == "__main__":
    herf = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"

    response = requests.post(url, data={"q": herf})

    try:
        data = response.json()
        if data == {}:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
    except ValueError:
        print("Not a valid JSON")
