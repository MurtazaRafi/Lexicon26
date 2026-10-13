from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["webshop"]

# print(client.list_database_names())

# print(db.list_collection_names())
# product = db.products.find_one()
# print(product)

# for name in db.list_collection_names():
#    print(name, db[name].count_documents({}))

# for customer in db.customers.find():
#    print(customer["first_name"], list(customer.keys()))

from pprint import pprint

#result = db.products.insert_one({"name":"Gloves", "category": "Accessories", "price": 199, "stock":20})
#print(result.inserted_id)
#pprint(db.products.find_one({"name": "Gloves"}), sort_dicts=False)

#result = db.products.delete_one({"name": "Gloves"})
#print("deleted", result.deleted_count)
#print(db.products.count_documents({}))

#product = db.products.find_one({"name": "Beanie"})
#print(product["name"], "costs", product["price"], "kr" )

#print(db.products.count_documents({}))
#print(db.products.count_documents({"category": "Shoes"}))
#print(db.customers.find())

#for customer in db.customers.find():
#    print(customer["first_name"], customer["last_name"])

#SELECT first_name FROM customers WHERE city = "Uppsala"
#for customer in db.customers.find():
#    print(customer["first_name"], customer.get("city", "unknown"))


#result = db.customers.insert_one({
#    "first_name": "Noah",
#    "last_name" : "Svensson",
#    "email": "noah@gmail.com",
#    "city": "Enköping"
#})

#print(result.inserted_id)

result = db.products.insert_many([
    {"_id":13, "name": "Scarf", "category": "Accessories", "price":299,
     "stock":15, "tags":["winter"], "details": {"color": "red"}},
     {"_id":14, "name": "Gloves", "category": "Accessories", "price":199,
          "stock":20, "tags":["winter"], "details": {"color": "black"}}
])

print(result.inserted_ids)
print(db.products.count_documents({}))