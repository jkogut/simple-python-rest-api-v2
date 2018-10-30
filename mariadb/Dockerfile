FROM mariadb:latest		

ENV MYSQL_ROOT_PASSWORD=password \
    MYSQL_DATABASE=titanic \
    MYSQL_USER=restuser \
    MYSQL_PASSWORD=restpassword

# WORKDIR /app-db
# RUN apt-get update -y && apt-get install python-pip -y \
#  && pip install csvkit \
#  && cd /app-db && /bin/sh normalize.sh 

EXPOSE 3306
