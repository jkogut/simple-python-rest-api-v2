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

`py.test -v -l test_rest_api_docker.py`
