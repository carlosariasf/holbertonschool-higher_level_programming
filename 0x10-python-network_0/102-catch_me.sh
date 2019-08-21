#!/bin/bash
#Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sL -X PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"
