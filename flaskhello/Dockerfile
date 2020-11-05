FROM golang:alpine as gobuilder
WORKDIR /go/src/app
COPY parent/main.go .
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build \
      -o /go/bin/parent .

FROM python:3.8-slim-buster
LABEL maintainer="Mike Lykov"
LABEL description="test task for testTeam"

ENV PYTHONUNBUFFERED="1" PYTHONDONTWRITEBYTECODE="1" 
ENV GUNICORNPORT="8080"

COPY --from=gobuilder /go/bin/parent /usr/local/bin

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install --upgrade pip && pip install -r \
		 /usr/src/app/requirements.txt

COPY . /usr/src/app

RUN useradd gunicorn && chown -R gunicorn /usr/src/app
USER gunicorn

ENTRYPOINT ["/usr/local/bin/parent"]
CMD ["/usr/local/bin/gunicorn", "--bind","0.0.0.0:${GUNICORNPORT}", "--worker-tmp-dir","/dev/shm","--workers=2","--threads=4","--worker-class=gthread","--log-file=-","--access-logfile=-","--log-level=info","mytestteamapp:mytestteamflask"]

