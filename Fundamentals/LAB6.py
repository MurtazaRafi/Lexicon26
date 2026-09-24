# Part A - List comprehensions
# 1.

numbers = range(1,21)
# squares = []
# for number in numbers:
#     squares.append(number ** 2)

# print(squares)

# list comp
squares = [number ** 2 for number in numbers]
print(squares)
# 2.
nums = range(1, 101)
even_numbers = [num for num in nums if num % 2 == 0]
print(even_numbers)
# 3.
names = ["adam larsson", "kalle karlsson", "eva engman"]
title_cased = [name.title() for name in names]
print(title_cased)
# # 4.
# scores = [100, 80, 70, 60]
# passed = [score for score in scores if score >=70]
# print(passed)
# 5.

scores = [100, 80, 70, 60]
passed = ["Pass" if score >=70 else "Fail" for score in scores]
print(passed)

# 6. Från lesson 3 5.
words = ["This", "is", "Python"]
count = 0
for word in words:
    if len(word) >= 5:
        count += 1
print(count)
# From lesson 4 3. 
def get_long_words(words, minimum_length):
    # long_words = []
    # for word in words:
    #     if len(word) >= minimum_length:
    #         long_words.append(word)

    long_words = [word for word in words if len(word) >= minimum_length]
    return long_words

print(get_long_words(["Hej", "Hallå"], 4))



# with list comp.
long_words = [word for word in words if len(word) >= 5]
print(len(long_words))


# Part B - Dictionary and set comprehensions
# 1. 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = {num: num ** 2 for num in nums}
print(squares)

# 2.

words = ["Life", "is", "Beautiful"]
word_lengths = {word : len(word) for word in words}
print(word_lengths) 

# 
# 3.
lst = ["Python", "C#", "Java", "Java", "Python"]
lower = {element.lower() for element in lst}
print(lower)

# 4.
products = [{"product" : "car", "price" : 100000}, {"product" : "bicycle", "price" : 5000}, {"product" : "motorcycle", "price" : 20000}]

cheep_products = {element["product"] : element["price"] for element in products if element["price"] <= 20000}

print(cheep_products)

# 5.
students = [{"name": "Olle", "score": 70}, {"name": "Volkan", "score": 60}, {"name": "Karl", "score": 85}]

passed = {student["name"] : "PASS" if student["score"] >= 70 else "FAIL" for student in students}

print(passed)

# part C - enumerate

# 1. 

playlist = ["Hej hej", "Vad är det här?", "Bästa"]

for index, song in enumerate(playlist, start = 1):
    print(index, song)

# 2. 

tasks = ["Laundry", "Study", "Eat", "Walk"]

for i, task in enumerate(tasks, start=1):
    print(f"Task {i}: {task}") 

# 3. 
for i, task in enumerate(tasks, start=1):
    if i >= 2:
        print(f"Task {i}: {task}") 

# 4. Cleaner because you get the index and the value directly

for i in range(len(tasks)):
    print(i, tasks[i])

# See above for better solution

# part D - zip and unpacking
# 1.
names = ["Anna", "Karl", "Murtaza"]
scores = [80, 60, 70]

students = zip(names, scores)

for student in students:
    print(student)

# 2.
print(dict(students))

# 3.
product_names =["bicycle", "motorbike", "car"]
prices = [5000, 20000, 100000]
stock = [100, 50, 20]

items = zip(product_names, prices, stock)
for item in items:
    print(item)
# 4.

users = zip(["name 1", "name 2", "name 3"], [100, 80])
for user in users:
    print(user)

# 5.
names = ["Anna", "Karl", "Murtaza"]
scores = [80, 60, 70]

student_dictionary = {}
for key, val in zip(*[names, scores]):
    student_dictionary[key] = val

print(student_dictionary)

# 6.
x = 2
y = 3
x, y = y, x

# part E - sorted and lambda
# 1.
words =["Hej", "Jag", "Heter", "Murtaza"]

print(sorted(words, key=len))

# 2.
students = [{"name": "Olle", "score": 70}, {"name": "Volkan", "score": 60}, {"name": "Karl", "score": 85}]
ascending = sorted(students, key = lambda student: student["score"])
descending = sorted(students, key = lambda student: student["score"], reverse=True)
print(ascending)
print(descending)

# 3. 
products = [{"product" : "car", "price" : 100000}, {"product" : "bicycle", "price" : 5000}, {"product" : "motorcycle", "price" : 20000}]


sortedd = sorted(products, key = lambda product: product["price"])
print(sortedd) 

# 4.
names = [{"first_name" : "Murtaza", "last_name" : "Rafi"}, {"first_name" : "Adam", "last_name" : "Karlsson"}]
sorted_by_last_name = sorted(names, key=lambda name: name["last_name"])
print(sorted_by_last_name)

# 5. 
people = [{"name" : "Murtaza", "age" : 65}, {"name" : "Adam", "age" : 45}]

def get_person_age(person):
    return person["age"]

print(sorted(people, key=get_person_age))
# Explananation: for each person in people - ta person["age"] och sortera baserad på den

print(sorted(people, key=lambda person: person["age"]))

# def 

print("########## PART F ##########")
# part F
# 1.
products = [
    {"name": "   Wireless Mouse ", "category": "      Electronics", "price": 24.99, "stock": 150},
    {"name": " headphones", "category": "electronics  ", "price": 79.99, "stock": 85},
    {"name": "    yoga Mat ", "category": " fitness", "price": 29.99, "stock": 200},
    {"name": "Stainless Steel Water Bottle  ", "category": " home & Kitchen", "price": 18.50, "stock": 320},
    {"name": "Mechanical keyboard", "category": "Electronics", "price": 89.99, "stock": 60},
    {"name": "Running Shoes ", "category": "Footwear ", "price": 64.99, "stock": 0},
    {"name": "Ceramic coffee mug", "category": "   Home & Kitchen    ", "price": 9.99, "stock": 400},
    {"name": "Backpack", "category": "   accessories", "price": 45.00, "stock": 0},
    {"name": "Desk lamp", "category": "Home & Office", "price": 32.99, "stock": 140},
    {"name": "Resistance bands Set", "category": "Fitness", "price": 15.99, "stock": 250},
    {"name": "  notebook  ", "category": " Stationery ", "price": 12.49, "stock": 0},
    {"name": "   power Bank", "category": " electronics    ", "price": 34.99, "stock": 175}]
# 2.
def normalize(name):
    return name.strip().title()

normalized_names = [normalize(product["name"]) for product in products]
normalized_categories = [normalize(product["category"]) for product in products]

# eller

normalized_products = [
    {
        **product,  # **product tar med allt, men name och category skrivs sen över med de normaliserade värdena. Resten behålls som dom är.
        "name" : normalize(product["name"]),
        "category" : normalize(product["category"])
    }
    for product in products
]
# print(normalized_products)
# 3.
in_stock = [product for product in products if product["stock"] > 0]
# print(in_stock)

# 4.
unique_categories = set(normalized_categories)
# print(unique_categories)

# 5.
inventory = {product["name"] : product["price"] * product["stock"] for product in products}
print(inventory)
# 6.
inventory_sorted = sorted(normalized_products, key=lambda product: product["price"] * product["stock"], reverse=True)
print("\n")
print(inventory_sorted)
# 7.
for index, product in enumerate(inventory_sorted, start=1):
    print(index, product)
# 8.
for name, category in zip(normalized_names, normalized_categories):
    print(name, category)
# part G
# 1.

# Med for-loop först
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
vector = []
for sublist in matrix:
    for element in sublist:
        vector.append(element)
print(vector)

# med list comprehension
flattened = [element for sublist in matrix for element in sublist]
print(flattened)
# [new_list for sublist in matrix]

# 2.

# 3.
students = [{"name": "Olle", "score": 70}, {"name": "Volkan", "score": 60}, {"name": "Karl", "score": 85}]
passed = [student for student in students if student["score"] >= 70]
print(passed)

# 4.

scores = [92, 20, 65, 60, 70, 90, 80]

def like_any(scores, matching_score):
    for score in scores:
        return score == matching_score

matching_score = 92

print(like_any(scores, matching_score))
print(any(element == matching_score for element in scores))
# If condition true for one element
treshold = 70
print(all(element >= treshold for element in scores))
# for all elements
