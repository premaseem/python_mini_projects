__author__ = 'asee2278'

from jsonschema import validate


schema = {
     "type" : "object",
     "properties" : {
         "price" : {"type" : "number"},
         "name" : {"type" : "string"},
     },
    "required": ["name"]
 }

validate({"name" : "Eggs", "price" : 34.99}, schema)

# Failing test
# validate({"name" : "Eggs", "price" : "34.99"}, schema)