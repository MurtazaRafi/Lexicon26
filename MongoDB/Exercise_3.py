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

orders = db.orders.aggregate([
   {
      "$lookup": {
         "from": "customers",
         "localField": "customer_id",
         "foreignField": "_id",
         "as": "customer"
      }},
    {"$unwind": "$customer"},
    {"$group": {"_id": "$customer",
                "orders": {"$sum": 1}}},
    {"$match" : {"orders" : {"$gte" : 2}}}
])

for order in orders:
    pprint(order)

# 7.

orders = db.orders.aggregate([
   { "$project": {
        "items": 1, 
        "items_count" : {"$size" : "$items"}
    }}
])

for order in orders:
    print(order["_id"], order["items_count"])
# 8.

units_by_category = db.orders.aggregate([
    {"$unwind": "$items"},
    {
      "$lookup": {
         "from": "products",
         "localField": "items.product_id",
         "foreignField": "_id",
         "as": "product_info"
      }},
    {"$unwind": "$product_info"},
    {"$group": {"_id": "$product_info.category",
            "total_units_sold": { "$sum": "$items.quantity" }}}
])

for category in units_by_category:
    pprint(category)
