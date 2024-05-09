#!/bin/bash
# accepts a URL and sends a request to that URL, displays the size
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
