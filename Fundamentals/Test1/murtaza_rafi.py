# ==================================================
# TASK 1
# ==================================================

products = [
    {"name": "Laptop", "price": 12000, "stock": 0},
    {"name": "Mouse", "price": 350, "stock": 0},
    {"name": "Keyboard", "price": 800, "stock": 6},
    {"name": "Monitor", "price": 3200, "stock": 3},
    {"name": "Headset", "price": 950, "stock": 0},
    {"name": "Webcam", "price": 1100, "stock": 5}
]

# 1. Loop through the products.
for product in products:
    print(product)
# 2. Print the name of every product that is in stock.
for product in products:
    if product["stock"] > 0:
        print(product["name"])

# 3. Calculate the total value of all products in stock.
#    The value of a product is price * stock.
def get_total(products):
    total = 0
    for product in products:
        if product["stock"] > 0:
            total += product["price"] * product["stock"]

    return total
# 4. Print the total value.
print(get_total(products))
# 5. Keep track of which in-stock product has the highest price
#    without using max(), and print its name.

def get_highest(products):
    highest = 0
    highest_product = products[0]
    for product in products:
        if product["price"] > highest and product["stock"] > 0:
            highest = product["price"]
            highest_product = product
    return highest_product

print("highest price:", get_highest(products))

# Write your solution below:





# ==================================================
# TASK 2
# ==================================================

scores = [78, 92, 55, 81, 67, 95, 73]

# Create a function called calculate_average that:
# - receives a list of scores
# - calculates and returns the average score
#
# Create another function called create_result that:
# - receives a list of scores
# - uses calculate_average()
# - returns "PASS" if the average is 70 or higher
# - otherwise returns "FAIL"
#
# Call create_result() using the scores above.
# Print both the average score and the final result.


# Write your solution below:

def calculate_average(scores):
    return sum(scores) / len(scores)

def create_result(scores):
    average = calculate_average(scores)

    if average >= 70:
        return "PASS"
    else:
        return "FAIL"

print("Average and Result", calculate_average(scores), create_result(scores))

# ==================================================
# TASK 3
# ==================================================

product_prices = [250, 400, 150, 700]

order_settings = {
    "discount": 10,
    "shipping": 49,
    "priority": True
}

# Create a function called calculate_order that:
# - receives a customer name as a normal parameter
# - receives any number of product prices using *args
# - receives optional settings using **kwargs
# - calculates the subtotal of all product prices
# - applies the discount percentage if "discount" exists
# - adds shipping if "shipping" exists
# - returns a dictionary containing:
#       customer
#       subtotal
#       final_total
#       settings
#
# Call the function using:
# - customer name "Anna"
# - the values from product_prices using unpacking
# - the values from order_settings using dictionary unpacking
#
# Print the returned dictionary.


# Write your solution below:

def calculate_order(customer_name, *prices, **optional_settings):
    subtotal = sum(prices)
    discount = optional_settings.get("discount") 
    total = 0
    if discount is not None:
        total = subtotal * (1 - discount / 100)
    shipping = optional_settings.get("shipping") 
    if shipping is not None:
        total += shipping

    return {"customer": customer_name, "subtotal": subtotal, "final_total": total, "settings": optional_settings }


dict = calculate_order("Anna", *product_prices, **order_settings )
print(dict)




# ==================================================
# TASK 4
# ==================================================

players = [
    {"name": "  anna", "score": 85, "active": True},
    {"name": "DAVID ", "score": 72, "active": False},
    {"name": " sara ", "score": 94, "active": True},
    {"name": "LEO", "score": 67, "active": True},
    {"name": " emma", "score": 88, "active": True},
    {"name": "OSCAR ", "score": 81, "active": False}
]

# 1. Create a new list containing normalized player names.
#    Remove unnecessary whitespace and use consistent capitalization.
#    Use a list comprehension.

# 2. Create a new list containing only the active players
#    with a score of 80 or higher.
#    Use a list comprehension.
#
# 3. Sort the original players by score from highest to lowest.
#    Use sorted() with a lambda.
#
# 4. Print the ranking in the following format:
#
#    1. Sara - 94
#    2. Emma - 88
#    ...
#
#    Generate the ranking numbers using enumerate().
#
# 5. Create a separate list containing the player names and
#    another list containing their scores.
#    Combine them using zip() and print each name together
#    with its score.


# Write your solution below:

# def normalize_name(name : str) -> str : 
#     trimmed = name.strip()
#     capitalized = name.capitalize()
#     return capitalized

# 1.
normalized_names = [player["name"].strip().capitalize() for player in players]

# 2.
active_players = [player for player in players if player["score"] >= 80 and player["active"]]
print(active_players)

# 3.
sorted_players = sorted(players, key=lambda player: player["score"], reverse=True)
print(sorted_players)

# 4.
for ranking, player in enumerate(sorted_players, start = 1):
    print(f"{ranking}. {player["name"]} - {player["score"]}")

# 5
scores = [player["score"] for player in players]

for name, score in zip(normalized_names, scores):
    print(name, score)