#!/usr/bin/python3
"""Display body of response, decoded in utf-8"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    with urllib.request.urlopen(url, data=email.encode('utf-8')) as response:
        print(response.read().decode('utf-8'))
