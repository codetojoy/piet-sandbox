#!/bin/bash

IMAGE_FILE=$1

docker run --rm -v "$PWD":/code:ro esolang/piet piet /code/$IMAGE_FILE
