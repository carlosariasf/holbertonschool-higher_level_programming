#!/bin/bash
#Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
body=$(curl -s $1)
len=${#body}
echo "$len"
