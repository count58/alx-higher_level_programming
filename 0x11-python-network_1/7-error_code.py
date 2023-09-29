#!/usr/bin/python3
""" script that takes in a URL, sends a request to
 the URL and displays the body of the response."""
 import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)
    response.raise_for_status()

    content = response.text
    print(content)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching URL: {e}")
