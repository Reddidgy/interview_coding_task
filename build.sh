#!/bin/bash

# if arg 1 equals --no-cache
if [ "$1" == "--no-cache" ]; then
  docker build --no-cache -t interview_coding_task_app .
else
  docker build -t interview_coding_task_app .
fi
