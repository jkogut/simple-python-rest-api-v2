FROM python:2.7
#COPY /app /app
WORKDIR /app
RUN apt-get update && apt-get install default-libmysqlclient-dev -y \
 && pip install --no-cache-dir flask flask-jsonpify flask-sqlalchemy flask-restful mysql-python
EXPOSE 5002
CMD sleep 15 && python ./rest_server.py
