#!/usr/bin/python3
"""Fetch https://alx-intranet.hbtn.io/status"""
import requests

def fetch_alx_intranet_status():
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.content.decode()
    print(f"Body response:\n\t- content: {content}")

if __name__ == "__main__":
    fetch_alx_intranet_status()
