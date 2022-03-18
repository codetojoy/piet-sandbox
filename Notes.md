
### Usage

* requires Docker and image at [1]
* from command-line: `./run.sh $IMAGE_FILE`
* from docker container:
    - `./debug.sh`
    - `# ~/npiet -cs 1 -t /code/$IMAGE_FILE`

### tmp notes 

in docker container
- ~/npiet -cs 9 -t /code/generator/print_q.png
    - 17-MAR-2022
    - prints Q but doesn't stop

### Resources

* [1] - Docker image: https://hub.docker.com/r/esolang/piet
* online interpreter: https://www.bertnase.de/npiet/npiet-execute.php
* https://www.bertnase.de/npiet/picture.html
* https://www.dangermouse.net/esoteric/piet.html
* Rust compiler: https://github.com/tessi/rpiet/ 
