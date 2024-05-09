#!/bin/bash
# sends a request to a URL passed as argument, displays status code of the response.
curl -o /dev/null -sw "%{http_code}" $1
