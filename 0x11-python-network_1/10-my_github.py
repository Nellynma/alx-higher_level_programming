#!/usr/bin/python3
"""Use GitHub API to display id"""
import requests
import sys

username = sys.argv[1]
password = sys.argv[2]
url = f"https://api.github.com/users/{username}"
response = requests.get(url, auth=(username, password))
if response.status_code == 200:
    user_id = response.json().get("id")
    print(f"Your user ID is: {user_id}")
else:
    print("Failed to retrieve user information")
