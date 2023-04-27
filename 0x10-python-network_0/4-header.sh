#!/bin/bash
# Script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
