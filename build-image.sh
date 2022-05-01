#!/bin/bash
target=btre

docker stop $target
docker rm -f $target
docker build -t $target .
docker run -d --restart=unless-stopped -p 8000:8000 --name=$target $target
docker logs -f $target