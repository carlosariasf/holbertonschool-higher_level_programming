#!/bin/bash
#Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
coderes=$(curl -s -o /dev/null -w "%{http_code}" -X GET $1)
if [ $coderes -eq 200 ]; then
    body=$(curl -sb -X GET $1)
fi
len=${#body}
echo "$len"
