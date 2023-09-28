#!/bin/bash
#takes in a URL as an argument, sends in the GET request to the URL,and displays the output body of the response
curl -sH "X-School-User-Id: 98" "$1"
