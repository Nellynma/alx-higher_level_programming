#!/usr/bin/python3
"""Take 2 arguments"""
import requests
import sys

repo_name = sys.argv[1]
owner_name = sys.argv[2]

response = requests.get(f"https://api.github.com/repos/{owner_name}/{repo_name}/commits")

for commit in response.json()[:10]:
    sha = commit['sha'][:7]
    author = commit['commit']['author']['name']
    print(f"{sha}: {author}")
