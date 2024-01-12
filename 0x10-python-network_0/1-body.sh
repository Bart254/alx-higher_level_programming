#!/bin/bash
#Displays body of response message only if the status is 200
CODE=$(curl -s -L -o /dev/null -w "%{http_code}" "$1");[[ $CODE == "200" ]] && curl -s -L "$1"
