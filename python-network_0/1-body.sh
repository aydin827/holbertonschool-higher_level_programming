#!/bin/bash
#fs
if [ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" -eq 200 ]; then
    curl -s "$1"
fi
