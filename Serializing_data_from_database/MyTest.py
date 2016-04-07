__author__ = 'asee2278'
import Main
import httplib2
import json


# tested just the function
print Main.getThings()

address = 'http://localhost:5000'

#Making a get call for things
print "Making a get call for things "

import requests
r = requests.get("http://localhost:5000/things")
print r.status_code
print r.content


try:
	url = address + "/things"
	h = httplib2.Http()
	resp, result = h.request(url, 'GET')
	#obj = json.loads(result)
	#puppyID = obj['Puppy']['id']
	if resp['status'] != '200':
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])

except Exception as err:
	print "Test 1 FAILED: Could not make POST Request to web server"
	print err.args
else:
	print "Test 1 PASS: Succesfully Made POST Request to /puppies"