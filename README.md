# simple-python-rest-api-v2

Simple python REST API v2 with docker and travis-ci

[![Build Status](https://travis-ci.org/jkogut/simple-python-rest-api-v2.svg?branch=master)](https://travis-ci.org/jkogut/simple-python-rest-api-v2)
[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)

Install
-------

clone the repo first and then build the docker images and run it

```
docker-compose up -d
```

test it with *py.test*

```
py.test -v -l test_rest_api_docker.py
```


Test
----

Test available endpoints with *curl*

 * [GET] API status *http://0.0.0.0:5002/api/status*
 * [GET] Passengers (Id,Name)  *http://0.0.0.0:5002/api/v1/passengers*
 * [GET] Passenger's Data (Id) *http://0.0.0.0:5002/api/v1/passengers/Id*
 * [GET] Survived Yes/No passengers *http://0.0.0.0:5002/api/v1/passengers/survived/0|1*
 * [POST] Create new employee *http://0.0.0.0:5002/api/v1/passengers/new*
 * [DELETE] Passenger (Id) *http://0.0.0.0:5002/api/v1/passengers/delete/passengerId*

Example usage:
```
curl http://0.0.0.0:5002/api/status |jq
curl http://0.0.0.0:5002/api/v1/passengers |jq
curl http://0.0.0.0:5002/api/v1/passengers/234 |jq
curl http://0.0.0.0:5002/api/v1/passengers/survived/1 |jq
curl -H "Content-Type: application/json" -X POST -d@payload.json http://0.0.0.0:5002/api/v1/passengers/new |jq
curl -X DELETE http://0.0.0.0:5002/api/v1/passengers/delete/887 |jq
```

Debug
-----

Clone the repo:

```
git clone git@github.com:jkogut/simple-python-rest-api-v1.git
```

Use `virtualenv` and install dependencies with `pip`:
```
virtualenv venv 
source venv/bin/activate
pip install -r app/requirements.txt
```

In `docker-compose.yml` file:
1. Comment out whole *rest-api-service* section and allow communication with MariaDB by uncommenting ports section in *mariadb-service*. 

2. Run *mariadb-service* and *normalize-db-service* containers with docker compose: `docker-compose up`

3. Edit `mysqlConf` variable and replace mariadb-service to *0.0.0.0* in `app/rest_server.py` file.

4. Run flask rest application in `debug mode`:
```
cd app;
python rest_server.py
```
