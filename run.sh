#!/usr/bin/env bash

if [ "$1" == "-b" ]; then
    docker build -t emelin .
fi

SOURCE_VOLUME="/home/marty/Projects/Emelin/src"
STATIC_VOLUME="/home/marty/Projects/Emelin/src/collect_static"
NGINX_VOLUME="/home/marty/Projects/Emelin/config/nginx"
EXPOSE_PORT=8001

if [ "$2" == "-p" ]; then
    SOURCE_VOLUME="/root/Emelin/src"
    STATIC_VOLUME="/root/Emelin/src/collect_static"
    NGINX_VOLUME="/root/Emelin/config/nginx"
    EXPOSE_PORT=8000
fi

echo $SOURCE_VOLUME

docker run -d --name emelin -v $SOURCE_VOLUME:/code emelin
docker run -d --name enginx -p $EXPOSE_PORT:8000 --link emelin:web -v $STATIC_VOLUME:/usr/share/nginx/html -v $NGINX_VOLUME:/etc/nginx/conf.d -d nginx