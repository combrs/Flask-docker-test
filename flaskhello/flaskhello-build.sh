#!/bin/bash

CONFIG=env_file_testteam
source ./$CONFIG
GUNICORNPORT=${GUNICORNPORT:-8080}
export GUNICORNPORT
DATE=$(date +%F)
UNIXTIME=$(date +%s)
VER=${UNIXTIME: -4}
export TAG=${DATE}-${VER}

[[ -f $CONFIG ]] || echo "GUNICORNPORT=${GUNICORNPORT}" > $CONFIG

if [[ -d parent ]]; then
    echo "'parent' go repo already cloned"
else
    git clone https://github.com/abiosoft/parent.git
fi    

envsubst '$GUNICORNPORT' < ./nginx.conf.template > ./nginx.conf


docker-compose build
docker-compose up -d --force-recreate

