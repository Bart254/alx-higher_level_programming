#!/bin/bash
#Displays only the status code 
curl -s -L -o /dev/null -w "%{http_code}" "$1"
