from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]
from pprint import pprint

# 1. 
# If its few reviews embed, but if thousands of reviews then its better to reference

# 2.
# Easier to show the inforamtion when embedded
# Disadvantage if need to change one proudct name and one has to change several one, one may miss someone

# 3. 
# db.create_collection("newsletter_signups", validator={"$jsonSchema": {
#  "required": ["email"],
#  "properties": {
#         "email" : {"bsonType": "string"},
#         "source": {
#           "enum": ['web', 'store']
#         }}}})

# products = db.newsletter_signups.insert_one({"email" : "murtazar@hotmail.com"})

# products = db.newsletter_signups.insert_one({"email" : ["murtazar@hotmail.com"]})

# 4.
result = db.customers.aggregate([{"$group" : 
                       {"_id" : "$city",
                        "customers" : {"$sum" : 1}}},
                        {"$sort" : {"city": -1}}])
for city in result:
    pprint(city)

# 5.
result2 = db.products.aggregate([{"$group" : 
                       {"_id" : "$category",
                        "category" : {"$sum" : 1},
                        "min_price" : {"$min": "$price"},
                        "max_price" : {"$max": "$price"}}}])
for product in result2:
    pprint(product)

# 6.
db.customers.aggregate([{"$group" : 
                       {"_id" : "$orders",
                        "" : {"$sum" : 1}}},
                        {"$sort" : {"city": -1}}])

