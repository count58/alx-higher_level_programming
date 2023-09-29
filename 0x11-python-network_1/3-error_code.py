#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""

import urllib.request
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        print(content)
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
