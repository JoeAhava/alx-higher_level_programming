#!/bin/bash
# script that takes in URL and sends a request to that URL and displays size of the body for the response
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
