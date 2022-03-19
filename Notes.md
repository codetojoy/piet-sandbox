
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

### TODO

* solve problem of running `./run.sh` and passing flags to inner `npiet`
* use CSS/SVG to create image?
* find simple pixel editor?
* ascii converter, using Pillow/python?

### Resources

* [1] - Docker image: https://hub.docker.com/r/esolang/piet
* online interpreter: https://www.bertnase.de/npiet/npiet-execute.php
* https://www.bertnase.de/npiet/picture.html
* https://www.dangermouse.net/esoteric/piet.html
* Rust compiler: https://github.com/tessi/rpiet/ 
