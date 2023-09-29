#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.

Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <username> <personal_access_token>")
    sys.exit(1)

username = sys.argv[1]
personal_access_token = sys.argv[2]

url = "https://api.github.com/user"

try:
    response = requests.get(url, auth=(username, personal_access_token))
    response.raise_for_status()

    user_info = response.json()
    user_id = user_info.get('id')

    print(f"Your GitHub user ID: {user_id}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching GitHub user information: {e}")
