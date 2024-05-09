#!/bin/bash
# accepts a URL and sends a request to that URL, displays the size
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
