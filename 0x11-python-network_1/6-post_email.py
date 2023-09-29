#!/usr/bin/python3
"""script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally displays
the body of the response.
"""
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}

try:
    response = requests.post(url, data=data)
    response.raise_for_status()

    content = response.text
    print(content)

except requests.exceptions.RequestException as e:
    print(f"Error sending POST request: {e}")
