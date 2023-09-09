#!/bin/bash

# if arg 1 equals --no-cache
if [ "$1" == "--no-cache" ]; then
  ./build.sh --no-cache
  docker build --no-cache -t test-image .
else
  docker build -t test-image .
fi

docker-compose up

