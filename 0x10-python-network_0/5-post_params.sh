#!/bin/bash
#Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST $1
