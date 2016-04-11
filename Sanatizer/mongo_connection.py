__author__ = 'asee2278'

import pymongo
from flask import Flask, jsonify
# from tweepy import API
#
# api = API()
# tweets = api.search('boobs',1)
# for tweet in tweets :
#     print tweet

from bson import json_util, ObjectId
import json

#Lets create some dummy document to prove it will work
page = {'foo': ObjectId(), 'bar': [ObjectId(), ObjectId()]}

#Dump loaded BSON to valid JSON string and reload it as dict
page_sanitized = json.loads(json_util.dumps(page))
print page_sanitized

# Connection to Mongo DB
try:
    conn=pymongo.MongoClient()
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e
conn

coll = conn.get_database('test').rules
#coll = testdb.get_collection()
bar = coll.insert_one({"find":"7.7.7.7 adminIP","replaceWith":"secretHost","rule_id":2,"isActive":False})
recs =  coll.find({},{'_id':0})
coll.update_many({"rule_id":2},{"$set" : { "find":"7.7.7.7 adminIP","replaceWith":"boobsUpdated","rule_id":2,"isActive":False} }  )
for rec in recs :
    print rec
