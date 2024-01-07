#!/bin/bash
#Returns the length of a curl request
curl -sI "${1}"| grep  Content-Length | awk '{print$2}'
