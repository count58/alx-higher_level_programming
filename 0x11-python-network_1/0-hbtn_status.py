#!/usr/bin/python3
import urllib.request

# Fetch the URL
with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:

    # Get the response body
    response_body = response.read().decode("utf-8")

    # Print the response body with tabulation before '-'
    print("\t-" + response_body)
