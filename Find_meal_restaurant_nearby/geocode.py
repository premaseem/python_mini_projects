__author__ = 'asee2278'


import httplib2
import json

def getLocation(inputString):
    locationString = inputString.replace(" ","+")
    googleApi="https://maps.googleapis.com/maps/api/geocode/json?address={loc}&key=AIzaSyAEMGjggKmZGi3hPI3k-fHQhPxrKJ3c_Dk".format(loc=locationString)
    url = (googleApi)
    response , content = httplib2.Http().request(url,"GET")
    #print content
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude,longitude)


# loc = raw_input("Enter the location you want coordinate for eg. pune, India")
#print "Cooridnate of your location {} are  ".format(loc) + str(getLocation(loc))
