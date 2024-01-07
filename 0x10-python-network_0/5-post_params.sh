#!/bin/bash
#Posts data to the server
curl -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
