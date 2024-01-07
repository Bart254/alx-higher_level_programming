#!/bin/bash
#Displays all the HTTP methods the server accepts
curl -sIX OPTIONS "$1"| awk '/Allow:/ {for(i=2; i<=NF; i++) { if (i == NF) print $i; else printf "%s ", $i}}' 
