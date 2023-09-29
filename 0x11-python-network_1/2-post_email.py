#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.

Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import urllib.request
import urllib.parse
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Prepare the data to be sent in the POST request
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

try:
    # Send a POST request to the specified URL
    with urllib.request.urlopen(url, data=data) as response:
        # Read and decode the body of the response
        content = response.read().decode('utf-8')
        print(content)
except urllib.error.URLError as e:
    print(f"Error sending POST request: {e}")
