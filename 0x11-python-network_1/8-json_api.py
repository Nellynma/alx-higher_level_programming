#!/usr/bin/python3
"""Send a request to http://0.0.0.0:5000/search_user"""
import requests
import sys

def search_user(letter):
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": letter}
    response = requests.post(url, data=data)
    try:
        if response.json():
            print("[{}] {}".format(response.json().get("id"), response.json().get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    try:
        letter = sys.argv[1]
    except IndexError:
        letter = ""
    search_user(letter)
