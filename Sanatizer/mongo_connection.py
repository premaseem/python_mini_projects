__author__ = 'asee2278'

import pymongo

# Connection to Mongo DB
try:
    conn=pymongo.MongoClient()
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e
conn

db = conn.get_database('test')
#coll = testdb.get_collection()
bar = db.rules.insert_one({'name':'prem'})
print bar
