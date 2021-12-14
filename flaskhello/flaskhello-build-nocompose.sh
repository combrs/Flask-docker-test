#!/bin/bash

DATE=$(date +%F)
UNIXTIME=$(date +%s)
VER=${UNIXTIME: -4}

if [[ -d parent ]]; then
    echo "'parent' go repo already cloned"
else
    git clone https://github.com/abiosoft/parent.git
fi    

docker build --network=host -t flaskhello:${DATE}-${VER} .
rm -rf parent/
CONT=$(docker ps -aq --filter name=flaskhello)
if [[ -z "$CONT" ]]; then
    echo "no 'flaskhello' containers to remove"
else
    docker rm -f $CONT
fi
docker run -d --net=host --rm --name flaskhello --env-file=env_file_baikalteam flaskhello:${DATE}-${VER}

