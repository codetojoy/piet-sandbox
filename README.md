### piet-sandbox

collecting some resources on the esoteric language, Piet

### Usage

* requires Docker and image at [1]
* from command-line: `./run.sh $IMAGE_FILE`
    - this isn't working yet, as we need to pass flags `-cs 1` to `npiet`
* from docker container:
    - `./debug.sh`
    - eg1: `# ~/npiet -cs 1 -t /code/$IMAGE_FILE`
    - eg2: `# ~/npiet -cs 1 /code/generator-py/print_q.png`
    - eg3: `# ~/npiet -cs 1 -t -v -e 10 /code/generator-py/print_q.png > out.log`
        - for trouble-shooting

### Index

Some programs (many are ultra-simple):

* print "Q" - `./generate-py/print_q.py` -> print_q.png
* print "Q" - `./generate-py/print_q_2.py` -> print_q_2.png
* print "Q" - ./images/print_q_3.png

### TODO

* solve problem of running `./run.sh` and passing flags to inner `npiet`
* use CSS/SVG to create image?
* ascii converter, using Pillow/python?

### Resources

* [1] - Docker image: https://hub.docker.com/r/esolang/piet
* [2] - Dockerfile: https://github.com/hakatashi/esolang-box/tree/master/boxes/piet
* online interpreter: https://www.bertnase.de/npiet/npiet-execute.php
* https://www.bertnase.de/npiet/picture.html
* https://www.dangermouse.net/esoteric/piet.html
* Rust compiler: https://github.com/tessi/rpiet/ 
