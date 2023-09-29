#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.

Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <repository_name> <owner_name>")
    sys.exit(1)

repository_name = sys.argv[1]
owner_name = sys.argv[2]

url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

try:
    response = requests.get(url)
    response.raise_for_status()

    commits = response.json()[:10]

    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching GitHub commits: {e}")
