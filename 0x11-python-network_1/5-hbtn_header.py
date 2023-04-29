#!/usr/bin/python3
"""Display X-Request-Id in response header"""
import requests
import sys

def get_request_id(url):
    response = requests.get(url)
    if response.status_code == 200:
        if 'X-Request-Id' in response.headers:
            request_id = response.headers['X-Request-Id']
            print(f"The value of X-Request-Id is: {request_id}")
        else:
            print("X-Request-Id header not found in the response")
    else:
        print(f"Request failed with status code: {response.status_code}")

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        url = args[1]
        get_request_id(url)
    else:
        print("Invalid arguments. Please provide only the URL as input")
