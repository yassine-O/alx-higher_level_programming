#!/bin/bash
#displays the body of the response
curl -s -o /dev/null -w '%{http_code}' $1
