from collections import Counter

# Part A - Function fundamentals
# 1.
def greet():
    print("Hello")
def show_course_name(name):
    print("Course:", name)
def print_seperator():
    print()

greet()
greet()
show_course_name("C#")
show_course_name("Python")
print_seperator
show_course_name("Java")
# 2.
def greet_person(name):
    print("hello", name)

def introduce(name, city):
    print(name + "lives in" + city)
# 3.
def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b
# 4.
# 5.
def calculate_area(width, height):  # <--- parameters 
    return width * height

print("Area is", calculate_area(5, 3))      # <--- Argument when calling the function

# part B - return values
# 1.
def is_even(number):
    return number % 2 == 0
print(is_even(2))
# 2.
def get_larger(a, b):
    if a > b:
        return a

    return b
print(get_larger(5,4))

# 3.
def classify_score(score):
    if score >= 70:
        return "PASS"
    return "FAIL"
print(classify_score(77))
# 4.
def full_name(first_name: str, last_name: str):
    """ returns full name"""
    return f"{first_name} {last_name}"

print(full_name("Murtaza", "Rafi"))
# 5.
def calculate_discount(price: int, percent: int) -> float:
    """Calculates discount and returns"""
    return price * percent / 100
print(calculate_discount(1000, 30))

# 6.
def print_function(name : str) -> None:
    """prints hello name"""
    print("hello", name)
# vs
def return_function(name):
    return "HEllo " + name

print_function("Murtaza")
#vs
print(return_function("Murtaza")) 

# Part C - Default and keyword arguments

# 1. 
def greet(name, greeting = 'Hello'):
    print(greeting, name)

greet("Murtaza", "Hi")
greet("Murtaza")
greet(greeting="Hej", name="Ola")

# 2.
def calculate_price(price, quantity = 1, discount = 0):
    return quantity * price - discount

# 3. 

def create_profile(name, city='Unknown', active = True):
    return {"name": name, "city": city, "active": active}
print(create_profile("Murtaza", "Stockohlm"))

# 4
print(calculate_price(500, discount=200, quantity=2))

# 5
# def greet(name = "Unknown", age):
#     print(name, age)


# part D - functions nad collections

# 1.
def calculate_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(calculate_total([1, 3, 10])) 

# 2.
def calculate_even(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count
print(calculate_even([1, 3, 10])) 

# 3. 
def get_long_words(words, minimum_length):
    long_words = []
    for word in words:
        if len(word) >= minimum_length:
            long_words.append(word)

    return long_words

print(get_long_words(["Hej", "Hallå"], 4))

# 4.
# Return the matching dictionary
def find_student(students, name):
    for student in students:
        if student["name"] == name:
            return student
    
students = [{"name": "Olle", "age": 30}, {"name": "Volkan", "age": 35}]

print(find_student(students, "Olle"))

# 5. 
def average_score(students):
    total = 0
    for student in students:
        total += student["score"]
    return total / len(students)

students = [{"name": "Anna", "score": 80}, {"name": "Anna2", "score": 85}]
print(average_score(students))

# 6.
def get_active_users(users):
    actives_users = []

    for user in users:
        if user["active"] == True:
            actives_users.append(user)
    return actives_users

users = [{"name": "Anna", "active": True}, {"name": "Karl", "active": True},
                    {"name": "Erik", "active": True}, {"name": "Anders", "active": False}]
print(get_active_users(users))

# part E - Decomposition
# 1. Temperature report
def celcius_to_fehrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

def classify(temperature_in_celcius):
    if temperature_in_celcius > 30:
        return "hot"
    elif temperature_in_celcius > 20:
        return "warm"
    else:
        return "cold"
def format(temperature, classification):
    print(f"The temperature is {temperature} and it is {classification}.")

temparature = 30
format(celcius_to_fehrenheit(temparature), classify(temparature))
# 2.
def discount(price, percentage):
    return price * (percentage / 100)

def subtotal(price, quantity):
    return price * quantity

def final_total(subtotal, discount):
    return subtotal - discount

# 3. part C2-3 as in E2-3 
# 4.
price = 15000
percentage = 30
quantity = 4

print(final_total(subtotal(price, quantity), discount(4 * price, percentage)))
# # Part G - Stretch challenges
# 1.
def min_max(numbers):
    largest = 0
    smallest = 1000 
    for number in numbers:
        if number > largest:
            largest = number

        if number < smallest:
            smallest = number
    return smallest, largest

numbers = [23,23,434,4,45]
smallest, largest = min_max(numbers)
print("smallest", smallest, "largest", largest)

# 2.
def is_palindrome(word):
    return word == word[::-1]

# word = input("Give a word for palindrome: ")
# print(is_palindrome(word))

# 3.
def character_count(word: str) -> dict[str, int]:
    """Counts characters of a string"""
    # return Counter(word)
    chars = {}
    for char in word:
        if char not in chars:
            chars[char] = 0
        chars[char] += 1
    return chars

print(character_count("HejHejHallå"))
# 4.

def organize_numbers(nums):
    organized = {"zeros": 0, "postives": 0, "negatives": 0}
    for num in nums:
        if num == 0:
            organized["zeros"] += 1

        if num > 0:
            organized["postives"] += 1

        if num < 0:
            organized["negatives"] += 1

    return organized

print(organize_numbers([4, -2, 4, 10, 0, -3]))

# 5.
# -

# Part F - Applied challenge: Event registration processor 
 
# 1. Create functions to normalize a participant name, validate an age range using boolean return values, calculate a registration fee based on age/student status, and create a participant dictionary. 
def normalize_name(name: str) -> str:
    stripped = name.strip()
    capitalized = stripped.capitalize()
    return capitalized
def ask_for_input(message):
    input = input(message)
    return input
def validate_age(age):
    if age >= 36:
        return True

    return False
def calculate_fee(age, status = True):
    valid_age = validate_age(age)

    if status and valid_age:
        return 2000
    elif not status and valid_age:
        return 3000
    elif status and not valid_age:
        return 4000
    return 5000 
def create_dictionary(name, age, status = True):
    return {"name": normalize_name(name), "age": age, "status": status, "fee": calculate_fee(age, status)}


# 2. Create at least eight participant dictionaries using your functions.

participant_1 = create_dictionary("Murtaza Rafi", 70, True) 
participant_2 = create_dictionary("Kalle Karlsson", 43, True) 
participant_3 = create_dictionary("Johan Ekberg", 60, False) 
participant_4 = create_dictionary("Bill Svensson", 50, True) 
participant_5 = create_dictionary("Abdi Raufi", 33, True) 
participant_6 = create_dictionary("Noor Sharifi", 25, False) 
participant_7 = create_dictionary("Arefa Bayat", 50, True) 
participant_8 = create_dictionary("Sven Rafi", 35, False) 
participant_9 = create_dictionary("Karl Soofi", 31, True) 
participants = [participant_1, participant_2, participant_3, participant_4, participant_5, participant_6, participant_7, participant_8, participant_9]
print(participants)
# 3. Write a function that receives the participant list and returns the total expected registration revenue.
def calculate_revenue(participants):
    total = 0
    for participant in participants:
        total += participant["fee"] 
    return total
print(calculate_revenue(participants))
# 4. Write a function that returns only student participants. 
# 5. Write a function that returns the oldest participant. 
def oldest_participant(participants):
    oldest = 0
    for participant in participants:
        if oldest < participant["age"]: 
            oldest = participant["age"]
    return oldest

print(oldest_participant(participants))
# 6. Write a function that creates a readable summary string for one participant. 
def create_summary(participant):
    summary = f"""This is a summary of participant: {participant["name"]}. He/She is {participant["age"]} years old and pays course fee {participant["fee"]}."""
    participant.__doc__ = summary

create_summary(participant_1)
print(participant_1.__doc__())
# 7. Keep input/output responsibilities separate from calculation functions as much as possible.

