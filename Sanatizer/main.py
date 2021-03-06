__author__ = 'Aseem Jain'

# This project is written in python, it sanitizes the input string by
# applying rules and return process out put. example a rule says to mask adminPassword then input file's
# admin password would be masked and replaced with the value from rule.

from flask import Flask, jsonify
import re
from flask import make_response
from flask import request
from pymongo import MongoClient
from bson import json_util, ObjectId


import pymongo

# Connection to Mongo DB

coll = pymongo.MongoClient().get_database('test').rules


fileString = """ This is line with adminPassword
This is line with password
This is line with 7.7.7.7 adminIP
This is line with 1.1.1.1 ip
This is line with network 7.7.7.7 details
This is line with public details """


rules=[{"find":"adminPassword", "replaceWith":"*****","rule_id":1, "isActive":True},
           {"find":"7.7.7.7 adminIP","replaceWith":"secretHost","rule_id":2,"isActive":False}
]

sanatiziedArray = []

def applyRule(line) :
    for rule in rules :
        line = re.sub(rule['find'],rule['replaceWith'],line)
        #print sanatizedLine
    sanatiziedArray.append(line)

def convert_array_to_file(arr):
    for line in arr :
        print line

def convert_file_to_arry(str):
    return str.split('\n')

def rule_application(dataArray):
    for line in dataArray :
        applyRule(line)

# file converted in array
dataArray = convert_file_to_arry(fileString)

rule_application(dataArray)

print convert_array_to_file(sanatiziedArray)




app = Flask(__name__)


from flask import abort

try:
    conn=pymongo.MongoClient()
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e
conn

coll = conn.get_database('test').rules

# return all rules
import json
@app.route('/rules', methods=['GET'])
def get_tasks():
    rulesM = coll.find({},{"_id":0})
    res = []
    for rule in rulesM :
        print rule
        res.append(rule)
    return jsonify({'rules': res})

# return specific rule
@app.route('/rules/<int:rule_id>', methods=['GET'])
def get_task(rule_id):
    # rule = [rule for rule in rules if rule['rule_id'] == rule_id]
    rule = coll.find_one({"rule_id": rule_id},{"_id":0})
    if rule is None or len(rule) == 0:
        abort(404)

    return jsonify({'rule': rule})


@app.route('/rules/<int:rule_id>', methods=['DELETE'])
def delete_task(rule_id):
    result = coll.remove({"rule_id":rule_id})
    if result is not None :
        return jsonify({"result":True})
    return jsonify({"result":False})


@app.route('/rules/add', methods=['POST'])
def add_rule():
    if not request.json or not 'find' in request.json:
        abort(400)
    jsonM = request.json
    l=[]
    l = coll.find().sort("rule_id",pymongo.DESCENDING)
    #rec = {"rule_id":69}
    new_id = l[0]["rule_id"] + 1
    jsonM["rule_id"] = new_id
    m_id = coll.insert_one(jsonM)
    print "Insert successful and mongo id is "  + str(m_id)
    #rules.append(rule)
    jsonM.pop("_id")
    return jsonify({'rule':jsonM }),201


@app.route('/rules/<int:rule_id>', methods=['PUT'])
def update_rule(rule_id):
    rule_to_update = coll.update({"rule_id":rule_id},request.json,False)
    result = True
    if rule_to_update["nModified"] == 0 :
        result=False
    return jsonify({'updated':result }),201


@app.route('/rules/<int:rule_id>', methods=['PATCH'])
def update_rule1(rule_id):
    rec = coll.find_one({"rule_id":rule_id})
    if rec is None :
        abort(404)
    for key in request.json.keys() :
        rec[key] = request.json[key]
    result = coll.update({"rule_id":rule_id},rec,False)
    print result
    return jsonify({"update":"success"})




@app.route('/rules/<int:rule_id>', methods=['PATCH'])
def update_rule2(rule_id):
    ruleList = [rule for rule in rules if rule['rule_id'] == rule_id]
    if len(ruleList) == 0:
            abort(404)
    if len(ruleList) ==0 :
        abort(404)
    rule_to_update = ruleList[0]
    print rule_to_update.keys()

# Except id all other data should get updated
    for key in request.json.keys() :
        if key == "rule_id" :
            continue
        rule_to_update[key] = request.json[key]
    return jsonify({'rule':rule_to_update }),201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(505)
def every_thing_ok(error):
    return make_response(jsonify({'error': 'Every thing ok '}), 505)


if __name__ == '__main__':
    app.run(debug=True)

