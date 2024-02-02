#!/bin/bash
# Posts json application file to a url
curl -sH "Content-Type: application/json" -d @"$2" "$1"
