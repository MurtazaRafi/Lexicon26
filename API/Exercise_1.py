# LAB 1
import requests
from pprint import pprint
from api_client import get_json


# response = requests.get("https://fakestoreapi.com/products")

# products = response.json()

# # sorted_products = sorted(products, key = lambda product: product["price"])

# # for product in sorted_products:
# #     print(product['title'], product['price'])



# # response2 = requests.get("https://fakestoreapi.com/products/categories")
# # categories = response2.json()
# # print(categories)

# user_category = input("Give a category: ")

# response3 = requests.get(f"https://fakestoreapi.com/products/category/{user_category}")

# # pprint(response3.json())
# products_by_category = response3.json()
# # Gives empty list

# product = sorted(products_by_category, key = lambda product: product["price"])[0]
# print("Number of products in this category:", len(products_by_category))
# print("cheapest product:", product["title"], product["price"])

# user_category = input("Give category: ")
# data = get_json(f"https://fakestoreapi.com/products/category/{user_category}")

# product = sorted(data, key = lambda product: product["price"])[0]
# print("Number of products in this category:", len(products_by_category))
# print("cheapest product:", product["title"], product["price"])


# 4. 
new_product = {
    "title": "Test product",
    'price': 13.5,
    'description': 'A product we create from Python',
    'image': 'https://champion.se/thumb/916/2560x0/CHBR220_1.webp',
    'category': 'electronics',
}

# POST
response = requests.post("https://fakestoreapi.com/products", json=new_product)
print(response.status_code)
print(response.json())

# PATCH

response4 = requests.patch("https://fakestoreapi.com/products/7", json={'price': 49.0})

response = requests.get("https://fakestoreapi.com/products/7")

print(response4.json())

# Vfr ändras ej priset??? Maybe bec false api

print(get_json("https://api.github.com/users/octocat")["name"])
get_json("https://api.github.com/users/this-user-does-not-exist-123")
get_json("https://api.github.com/users/octocat", timeout=0.001)
get_json("https://this-domain-does-not-exist-abc123.com")
get_json("fakestoreapi.com/products")
get_json("https://example.com")


# LAB2
# 1. 2.
def find_city(name):
    try:
        coordinates = get_json("https://geocoding-api.open-meteo.com/v1/search", params={"name" : name, "count" : 1})
        latitude, longitude = coordinates["results"][0]["latitude"], coordinates["results"][0]["longitude"]
        return latitude, longitude
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print("API returned a 404 error: Not Found")
        else:
            print("API returned an error:", e)
    except Exception as e:
        print("An error occurred:", e)


def get_weather(latitude, longitude):
    weather = get_json("https://api.open-meteo.com/v1/forecast", params={"latitude" : latitude , "longitude" : longitude, "current" : {"temperature_2m", "wind_speed_10m"}})

    temperature_2m = str(weather['current']['temperature_2m']) + ' ' + weather['current_units']['temperature_2m']

    wind_speed_10m = str(weather['current']['wind_speed_10m']) + ' ' + weather['current_units']['wind_speed_10m']

    return temperature_2m, wind_speed_10m

# 3.

name = input("Give a city: ")
latitude, longitude = find_city(name)
temp, wind = get_weather(latitude, longitude)
print(latitude)
print(f"{name}, Sweden: {temp}, wind {wind}.")

# 4.



