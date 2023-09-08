#!/bin/bash

# if arg 1 equals --no-cache
if [ "$1" == "--no-cache" ]; then
  ./build.sh --no-cache
else
  ./build.sh
fi

docker-compose down && docker-compose up -d