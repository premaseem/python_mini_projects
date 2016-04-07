from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()
db = client.test

@app.route("/")
def api_response():
    if request.method == 'GET':
        return "Welcome to page "


@app.route("/things",methods= ['GET'])
@app.route("/dicks")
def getThings() :
  cursor = db.things.find()
  data = []
  dict = {}
  for document in cursor:
    document['_id']= str(document['_id'])
    data.append(document)
    dict['data'] = data

  return jsonify(dict)



if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)