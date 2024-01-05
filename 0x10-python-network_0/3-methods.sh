#!/bin/bash
#takes in a URL and displays all HTTP methods the server will accept.
curl -s -i -X OPTIONS "$url" | grep -i 'allow' | cut -d':' -f2 | tr -d '[:space:]'
