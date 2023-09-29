#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.

Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
import requests
import sys

if len(sys.argv) == 1:
    q = ""
else:
    q = sys.argv[1]

data = {'q': q}

try:
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)
    response.raise_for_status()

    try:
        result = response.json()

        if result:
            print("[{}] {}".format(result.get('id'), result.get('name')))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")

except requests.exceptions.RequestException as e:
    print(f"Error sending POST request: {e}")
