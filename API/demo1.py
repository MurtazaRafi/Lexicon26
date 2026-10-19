# import requests

# response = requests.get("https://fakestoreapi.com/products")
# print(response)
# print(response[0])

# status code....headers....body

# print(response.status_code)
# print(response.headers["Content-Type"])
# print(response.text[:200])

# print(response.text[0]['title'])

# data = response.json()

# print(type(data))
# print(len(data))
# print(data[0])

# for product in data[:5]:
#     print(f"{product['id']}: {product['title']} - ${product['price']}")


# response = requests.get("https://fakestoreapi.com/products/15")
# product = response.json()
# print(product)
# print(product['rating'])
# print(product['rating']['rate'])
# print(product['title'], product['rating']['rate'])


# QUERY PARAMETERS

# import requests

# response = requests.get("https://fakestoreapi.com/products?limit=5")
# print(len(response.json()))


# response = requests.get("https://fakestoreapi.com/products", params={"limit": 5, "sort": "desc"})
# product = response.json()
# print(len(response.json()))
# print(response.url)
# print([product['id'] for product in response.json()])



# response = requests.get("https://fakestoreapi.com/products/categories")
# print(response.json())


# response = requests.get("https://fakestoreapi.com/products/", headers={'Accept': "application/json"})
# print(response.status_code)


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# 404

# import requests

# response = requests.get("https://api.github.com/users/octocat")
# print(response.status_code)
# print(response.json()['name'])


# response = requests.get("https://api.github.com/users/this-user-does-not-exist-123")
# print(response.status_code)
# print(response.json())



# response = requests.get("https://api.github.com/users/this-user-does-not-exist-123")

# if response.status_code == 200:
#     print(response.json(['name']))
# elif response.status_code == 404:
#     print("That user does not exist")
# else:
#     print(f"Something went wrong: {response.status_code}")

#raise_for_status()

# try:
#     response = requests.get("https://api.github.com/users/this-user-does-not-exist-123")
#     response.raise_for_status()
#     print(response.json()['name'])
# except requests.exceptions.HTTPError as error:
#     print(f"The server said no: {error.response.status_code}")
    


# response = requests.get("https://api.github.com/users/octocat", timeout=0.001)


# response = requests.get("https://this-domain-does-not-exist-abc123.com")

# response = requests.get("fakestoreapi.com/products")


# response = requests.get("https://example.com")
# print(response.status_code)
# response.json()



def get_json(url, params=None, headers=None, timeout=5):
    try:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("The request took too long")
    except requests.exceptions.ConnectionError:
        print("Could not connect to the server")
    except requests.exceptions.HTTPError as error:
        print(f"The server said no: {error.response.status_code}")
    except requests.exceptions.JSONDecodeError:
        print("The answer was not JSON")
    except requests.exceptions.RequestException as error:
        print(f"Someting else went wrong: {type(error).__name__}")
    return None


# print(get_json("https://api.github.com/users/octocat")["name"])
# get_json("https://api.github.com/users/this-user-does-not-exist-123")
# get_json("https://api.github.com/users/octocat", timeout=0.001)
# get_json("https://this-domain-does-not-exist-abc123.com")
# get_json("fakestoreapi.com/products")
# get_json("https://example.com")


# data = get_json("https://api.github.com/users/octocat")
# if data is not None:
#     print(data['name'])



# #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# import requests

# title, price, description, image, category

# POST

# new_product = {
#     "title": "Test product",
#     'price': 13.5,
#     'description': 'Aproduct we create from Python',
#     'image': 'https://champion.se/thumb/916/2560x0/CHBR220_1.webp',
#     'category': 'electronics',
# }

# response = requests.post("https://fakestoreapi.com/products", json=new_product)
# # print(response.status_code)
# # print(response.json())
# print(response.request.headers['Content-Type'])
# print(response.request.body)


# response = requests.post("https://fakestoreapi.com/products", data=new_product)
# # print(response.status_code)
# # print(response.json())
# print(response.request.headers['Content-Type'])
# print(response.request.body)

# PUT

# updated_product = {
#     "title": "Updated product",
#     'price': 99.0,
#     'description': 'New description',
#     'image': 'https://champion.se/thumb/916/2560x0/CHBR220_1.webp',
#     'category': 'electronics',
# }

# response = requests.put("https://fakestoreapi.com/products/7", json=updated_product)
# print(response.status_code)
# print(response.json())

# PATCH

# response = requests.patch("https://fakestoreapi.com/products/7", json={'price': 49.0})
# print(response.status_code)
# print(response.json())


# DELETE

# response = requests.delete("https://fakestoreapi.com/products/6")
# print(response.status_code)
# print(response.json())

# Let's check

# response = requests.get("https://fakestoreapi.com/products/7")
# print(response.json()['title'])
# response = requests.get("https://fakestoreapi.com/products/6")
# print(response.json()['title'])



#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

import requests

# response = requests.get("https://api.github.com/users/octocat")
# print(response.headers["X-RateLimit-Limit"])
# print(response.headers["X-RateLimit-Remaining"])

# response = requests.get("https://api.github.com/user")
# print(response.status_code)
# print(response.json())


# headers = {"Authorization": "Bearer THIS_IS_A_FAKE_TOKEN"}
# response = requests.get("https://api.github.com/user", headers=headers)
# print(response.status_code)
# print(response.json())


import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GITHUB_TOKEN")
headers = {"Authorization": f"Bearer {token}"}
response = requests.get("https://api.github.com/user", headers=headers)
print(response.status_code)
print(response.json()['login'])

# print(token is None)