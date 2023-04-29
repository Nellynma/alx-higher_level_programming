#!/usr/bin/python3
"""Send request to URL"""
import urllib.request
import urllib.error
import sys

def fetch_url_body(url):
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
        return None

if __name__ == "__main__":
    url = sys.argv[1]
    body = fetch_url_body(url)
    if body is not None:
        print(body)
