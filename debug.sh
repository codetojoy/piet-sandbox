#!/bin/bash

docker run -it --rm -v "$PWD":/code:ro esolang/piet sh

# e.g. piet /code/hello.piet.png
# note `piet` is just a script, so to get flags:
# ~/npiet -t /code/generator/hello.piet.png
