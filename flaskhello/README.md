
FlaskHello

Test task flask application for testTeam.
This archive contains two shell scripts:
flaskhello-build-nocompose.sh  flaskhello-build.sh

flaskhello-build-nocompose.sh - build and run a single container with app and gunicorn using "docker build & docker run"
flaskhello-build.sh  - build and run all needed to use nginx frontend proxy for gunicorn container with app
No arguments needed. 

There is an env file "env_file_testteam", which contains configurable port number for gunicorn and nginx proxy_pass.
It demonstrates how to configure containers from external source.

For start app unarchive contents on host with installed docker&docker-compose (tar -xf flaskhello.tar), set desired port (or leave it default 8080) 
and run flaskhello-build.sh. ocker-compose ends with
Creating gunicorn_flaskhello ... done
Creating nginx_flaskhello    ... done

check it with docker-compose ps (it must be "Up"):
gunicorn_flaskhello   /usr/local/bin/parent /usr ...   Up                        
nginx_flaskhello      nginx -g daemon off;             Up      0.0.0.0:80->80/tcp

check resulting nginx config with:
docker exec -it nginx_flaskhello nginx -T
see
...
proxy_pass http://gunicorn:<port>/;

check it with curl:
curl -sv localhost:
...
< HTTP/1.1 200 OK
Hello World from Mike Lykov for test task for testTeam!
check it with ab:
ab -n 1000 -c 4 localhost/
...
Requests per second:    928.61 [#/sec] (mean)

stop and remove it:
docker-compose down
...
Stopping nginx_flaskhello    ... done
Stopping gunicorn_flaskhello ... done
Removing nginx_flaskhello    ... done
Removing gunicorn_flaskhello ... done


