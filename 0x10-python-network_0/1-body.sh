#!/bin/bash
# takes in a URL, sends GET request, and displays the response
curl -sfL "$1" -X GET
