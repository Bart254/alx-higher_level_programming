#!/bin/bash
#Returns the length of a curl request
curl -sI "${1}"|  awk '/^Content-Length/ {print$2}'
