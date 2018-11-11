# simple-python-rest-api-v2

Simple python REST API v2 with docker and travis-ci

[![Build Status](https://travis-ci.org/jkogut/simple-python-rest-api-v2.svg?branch=master)](https://travis-ci.org/jkogut/simple-python-rest-api-v2)


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
 * [GET] Survived Yes/No passengers *http://0.0.0.0:5002/api/v1/passengers/survived/0|1*
 * [POST] Create new employee *http://0.0.0.0:5002/api/v1/passengers/new*
 * [DELETE] Delete passneger (Id) *http://0.0.0.0:5002/api/v1/passengers/delete/passengerId*

Example usage:
```
curl http://0.0.0.0:5002/api/status |jq
curl http://0.0.0.0:5002/api/v1/passengers |jq
curl http://0.0.0.0:5002/api/v1/passengers/survived/1 |jq
curl -H "Content-Type: application/json" -X POST -d@payload.json http://0.0.0.0:5002/api/v1/passengers/new |jq
curl -H "Content-Type: application/json" -X DELETE http://0.0.0.0:5002/api/v1/passengers/delete/887 |jq
```
