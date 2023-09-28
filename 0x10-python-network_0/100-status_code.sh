#!/bin/bash
#sends in a request to a URL passed as an argument, and displays only the status code of the output response.
curl -s -o /dev/null -w "%{http_code}" "$1"
