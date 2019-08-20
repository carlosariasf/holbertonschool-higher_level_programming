#!/bin/bash
#Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
#coderes=$(curl -sL -o /dev/null -w "%{http_code}" -X GET $1)
#if [ $coderes -eq 200 ]; then
#curl -sL -X GET $1
#fi
curl -sLi 34.206.234.184:46063/route_1 | tail -1
