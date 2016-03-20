__author__ = 'asee2278'

import httplib2
import json

def getLocation(inputString):
    locationString = inputString.replace(" ","+")
    googleApi="https://maps.googleapis.com/maps/api/geocode/json?address={loc}&key=AIzaSyAEMGjggKmZGi3hPI3k-fHQhPxrKJ3c_Dk".format(loc=locationString)
    url = (googleApi)
    response , content = httplib2.Http().request(url,"GET")
    print content
    #result = json.load(content)
    #print result
    print response


getLocation("pune India")

