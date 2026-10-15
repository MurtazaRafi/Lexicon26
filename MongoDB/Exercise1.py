from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# 1. 
products = db.products.find({"category" : "Accessories"});

for product in products:
    print(product["name"])

# 2.
customers = db.customers.find({"city" : "Göteborg"});

for customer in customers:
    print(customer["first_name"], customer["last_name"])
 
# 3.
for product in db.products.find():
    print(product["name"], product["price"])
# 4.
customers_count = db.customers.count_documents({"city" : "Uppsala"})
print(customers_count, "customers in Uppsala")

# 5.

sandals = db.products.find_one({"name" : "Sandals"})

print(sandals["stock"])
# 6.

gets_newsletter = db.customers.find({"newsletter" : True})

for customer in gets_newsletter:
    print(customer["first_name"])

# 7
# result = db.customers.insert_one({
#     "first_name": "Murtaza",
#     "last_name": "Rafi",
#     "email": "murtaza.rafi@example.com",
#     "city": "Stockholm"})
# pprint(result.inserted_id)

me = db.customers.find_one({"email": "murtaza.rafi@example.com"})
pprint(me)

# 8.
# db.products.insert_many([
#     {"_id":13, "name": "Scarf", "category": "Accessories", "price":299,
#          "stock":15, "tags":["winter"]},
#          {"_id":14, "name": "Gloves", "category": "Accessories", "price":199,
#               "stock":20, "tags":["winter"]}
# ])

print(db.products.count_documents({}))

# 9.

for customer in db.customers.find():
    print(customer["first_name"], customer["last_name"], customer.get("city", "unknown"))

# 10.

for order in db.orders.find():
    print(order["_id"], len(list(order["items"])))