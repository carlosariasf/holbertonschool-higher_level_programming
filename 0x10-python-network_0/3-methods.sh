#!/bin/bash
#Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
echo "$(curl -si $1)" | sed -n -e 's/^.*Allow: //p'
