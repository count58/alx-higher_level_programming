#!/usr/bin/python3
#takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.Usage: ./1-hbtn_header.py <URL>
import urllib.request
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)
except urllib.error.URLError as e:
    print(f"Error fetching URL: {e}")
