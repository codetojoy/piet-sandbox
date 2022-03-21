#!/bin/bash

IMAGE_FILE=$1

if [ -n "$1" ]; then
IMAGE_FILE=$1
else
  echo "usage: image file"
  exit -1
fi

if [ ! -f "$IMAGE_FILE" ]; then
echo "could not find specified file: ${IMAGE_FILE}"
else 
###########################
### run in Docker container
# original:
docker run --rm -v "$PWD":/code:ro esolang/piet piet /code/$IMAGE_FILE
# docker run --rm -v "$PWD":/code:ro esolang/piet piet "-cs 1 -t -e 10 /code/$IMAGE_FILE"
fi
