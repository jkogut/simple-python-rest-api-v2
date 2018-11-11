"""
python REST api tests with py.test
"""

__author__     = "Jan Kogut"
__copyright__  = "Jan Kogut"
__license__    = "MIT"
__version__    = "0.0.1"
__maintainer__ = "Jan Kogut"
__status__     = "Beta"

import requests
import json

##############################
# Config section starts here #
##############################

class TestConfig(object):
    pass

tstcfg = TestConfig()
tstcfg.apiUrl = 'http://0.0.0.0:5002/api'

##############################
# Tests section starts here  #
##############################

## GET API STATUS
class TestApiStatus(object):
    """ test API status """

    def test_apiGetStatus(self):
        """ test API GET status """

        url = tstcfg.apiUrl + '/status'
        r = requests.get(url)
        assert r.json()['API_status'] == 'OK'

        
## GET      
class TestApiGet(object):
    """ test API GET responses """

    def test_apiGetPassengers(self):
        """ test API GET Passengers """

        url = tstcfg.apiUrl + '/v1/passengers'
        r = requests.get(url)
        assert type(r.json()) is dict

        
    def test_apiGetSurvived(self):
        """ test API GET surived passengers based on survived status 0 or 1 """

        url = tstcfg.apiUrl + '/v1/passengers/survived/1'
        r = requests.get(url)
        assert type(r.json()) is list

        
## POST
class TestApiPost(object):
    """ test API POST responses """

    def test_apiPostFakePassenger(self):
        """ test API POST with new fake passenger creation """

        url = tstcfg.apiUrl + '/v1/passengers/new'

        with open('app/fake_payload.json', 'r') as f:
            payload = json.load(f)
            r = requests.post(url, json=payload)
            assert r.status_code == 400 # BAD REQUEST


    def test_apiPostNewPassenger(self):
        """ test API POST with new passenger creation """

        url = tstcfg.apiUrl + '/v1/passengers/new'

        with open('app/payload.json', 'r') as f:
            payload = json.load(f)
            r = requests.post(url, json=payload)
            assert r.status_code == 201 # CREATED


## DELETE
class TestApiDelete(object):
    """ test API DELETE responses """

    def test_apiDeleteNonExistentPassenger(self):
        """ test API DELETE with non existent passenger's Id """

        urlGet = tstcfg.apiUrl + '/v1/passengers'    
        rGet = requests.get(urlGet) # GET all passengers
        passNum = len(rGet.json()) # count them
        passNum = passNum + 100 # be sure Id is non existent
        urlDel = tstcfg.apiUrl + '/v1/passengers/delete/' + str(passNum) 
        rDelete = requests.delete(urlDel) # DELETE non existent passenger 
        assert rDelete.status_code == 400 # BAD REQUEST

        
    def test_apiDeletePassenger(self):
        """ test API DELETE with passenger's Id """

        with open('app/payload.json', 'r') as f:
            payload = json.load(f)
            passengerName = payload['Name']

        urlGet = tstcfg.apiUrl + '/v1/passengers'    
        rGet = requests.get(urlGet) # GET all passengers
        passId = rGet.json()[passengerName] # find his Id
        urlDel = tstcfg.apiUrl + '/v1/passengers/delete/' + str(passId) 
        rDelete = requests.delete(urlDel) # DELETE passenger 
        assert rDelete.status_code == 200 # OK
