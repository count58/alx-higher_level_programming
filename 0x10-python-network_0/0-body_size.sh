#!/bin/bash
#takes the URL, sends a request to that URL,and shows the size of the body of the response
curl -s "$1" | wc -c
