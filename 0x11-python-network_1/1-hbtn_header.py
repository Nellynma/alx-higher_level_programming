#!/usr/bin/python3
"""Display value of X-Request-Id variable""" 
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        x_request_id = res.getheader('X-Request-Id')
        print(x_request_id)
