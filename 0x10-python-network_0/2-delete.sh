#!/bin/bash
# sends the DELETE request to the URL that was passed as the first argument and displays the body of the response as output
curl -sX DELETE "$1"
