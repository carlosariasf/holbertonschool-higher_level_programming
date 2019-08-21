#!/bin/bash
#Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sd @"$2" -H "Content-Type: application/json" -X POST "$1"
