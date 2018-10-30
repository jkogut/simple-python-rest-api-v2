FROM python:alpine3.7

WORKDIR /app-db

RUN apk add --no-cache mariadb-client \
 && pip install csvkit

WORKDIR /app-db

CMD /bin/sh normalize.sh mariadb-service 33906
