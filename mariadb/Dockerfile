FROM mariadb:latest		

ENV MYSQL_ROOT_PASSWORD=password \
    MYSQL_DATABASE=titanic \
    MYSQL_USER=restuser \
    MYSQL_PASSWORD=restpassword

## in case you need to normalize DB localy
# WORKDIR /app-db
# RUN apt-get update -y && apt-get install python-pip -y \
#  && pip install csvkit \
#  && cd /app-db && /bin/sh normalize.sh 

EXPOSE 3306
