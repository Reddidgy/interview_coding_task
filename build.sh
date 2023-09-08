#!/bin/bash

# if arg 1 equals --no-cache
if [ "$1" == "--no-cache" ]; then
  docker build --no-cache -t my_terminal .
else
  docker build -t my_terminal .
fi
