# # Part A -basics
# # 1.
from sqlite3 import Date


# print("Murtaza Rafi")
# print("Python and ai")
# print("warm  up")

# # 2.
# name = "Murtaza Rafi"
# age = 20
# height = 1.73
# isStudent = True

# print(f"{name} type: {type(name)}")
# print(f"{age} type: {type(age)}")
# print(f"{height} type: {type(height)}")
# print(f"{isStudent} type: {type(isStudent)}")

# # 3.
# # Python is dynamically typed, it implicitly figures out. (And strongly typed). NEed to convert

# print(f"before conversion: {age} type: {type(age)}")
# print(f"after conversion: {str(age)} type: {type(str(age))}")

 
# # 4.
# # Arithmetics
# a, b = 5, 2
# print(f"addition: {a} + {b} = {a + b}")
# print(f"subtraction: {a} - {b} = {a - b}")
# print(f"multiplication: {a} * {b} = {a * b}")
# print(f"division: {a} / {b} = {a / b}")
# print(f"floor division: {a} // {b} = {a // b}")
# print(f"modulus: {a} % {b} = {a % b}")
# print(f"{a} ** {b} = {a ** b}")


# # 5.

# # three examples:
# #a) nr to str for printing purposes
# print("Age: " + str(age))

# #b) str to int for calcuations
# print(f"Age in 5 years: {age + 5}")

# #c) int to float for clearity
# print(f"Height in meters: {float(height)} m")


# Part B - User input and calculations
# 1.
# user_input = input("Enter your year of birth: ")
# age = Date.today().year - int(user_input)
# print(f"Your age is: {age}")

# 2.
# price = float(input("Enter price: "))
# discount = float(input("Enter discount percentage: "))

# discounted_price = price - price * (discount / 100)

# print(f"Discounted price: {round(discounted_price, 2)}")

# 3.
# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32

# print(f"Temperature in Fahrenheit: {fahrenheit}")

# 4.
# print("Give me the length and width of a room:")
# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))
# area = length * width
# print(f"The area of the room is: {area}")
# print(f"The perimeter of the room is: {2 * (length + width)}")

# 5.
# input("Give me a nr: ")
# It would interpret it as a string, can't do arithmetics   

# Part C - Strings
# 1. 
# sentence = "   Python is a great programming language.  "
# print(f"Length of the sentence: {len(sentence)}")
# print(f"Upper case: {sentence.upper()}")
# print(f"Lower case: {sentence.lower()}")
# print(f"Remove whitespace: {sentence.strip()}")

# # 2.
# firstname = input("Enter your first name: ")
# lastname = input("Enter your last name: ")
# fullname = f"{firstname} {lastname}"

# 3. 
s = 'python programming'

print(f"First character: {s[0]}")
print(f"Last character: {s[-1]}")
print(f"First 6 characters: {s[:6]}")
print(f"Last 11 characters: {s[-11:]}")
print(f"Reversed: {s[::-1]}")

# 4.
# def username_generator():
#     first_name = input("Enter your first name: ")
#     last_name = input("Enter your last name: ")

#     username = f"{first_name.strip()[:3].lower()}{last_name.strip()[:5].lower()}"
#     return username

# print(username_generator())

# 5.
# email = input("Enter your email address: ")
# username, domain = email.split('@')
# print(f"Your username is: {username}")
# print(f"Domain name is: {domain}")

# 6
# sentence = "Java is a great programming language."
# changed_sentence = sentence.replace("Java", "Python")
# print(f"Original sentence: {sentence}")
# print(f"Changed sentence: {changed_sentence}")

# Part D - String Investigation

# 1. slicing and indexing
# alphabets = "abcdefghij"
# print(f"First character: {alphabets[0]}")
# print(f"Last character: {alphabets[-1]}")
# print(f"First 3 characters: {alphabets[:3]}")
# print(f"Last 3 characters: {alphabets[-3:]}")
# print(f"Reversed: {alphabets[::-1]}")
# print(f"Every second character: {alphabets[::2]}")
# print(f"Every second character reversed: {alphabets[::-2]}")
# print(f"Characters from index 2 to 7: {alphabets[2:8]}")

# 2. 
 # ai = "Artificial Intelligence"
# print(f"First character: {ai[0]}")
# print(f"Last character: {ai[-1]}")
# print(f"First 3 characters: {ai[:3]}")
# print(f"Last 3 characters: {ai[-3:]}")
# print(f"Reversed: {ai[::-1]}")
# print(f"Every second character: {ai[::2]}")
# print(f"Every second character reversed: {ai[::-2]}")
# print(f"Characters from index 2 to 7: {ai[2:8]}")

# 3.
# data = "num=10"
# field, value = data.split('=')

# print(f"Field: {field}")
# print(f"Value: {value}")

# # data formatting - use replace to make data in array similar e.g.

# sentence = "Python is a great programming language."
# changed_sentence = sentence.replace("Python", "Java")

# 4.
# Immutable   
# my_string = "hej"
# my_string = "H" + my_string[1:]  # This creates a new string with the first character capitalized
# print(my_string)  # Output: Hej

# # PART E - Applied callange: Registration summary
# # 1. 2.
# def ConsoleProgram():
#     first_name = input("Enter your first name: ").strip()
#     last_name = input("Enter your last name: ").strip()
#     city = input("Enter your city: ").strip()
#     year_of_birth = int(input("Enter your year of birth: ").strip())
#     favorite_programming_language = input("Enter your favorite_programming_language: ").strip()
# #3.
#     user_id = f"{first_name.lower()}{last_name.lower()}{year_of_birth}"

# # 4. 
#     registration_summary = f"""
#     Summary of the registration:
#     Name: {first_name} {last_name}
#     City: {city}
#     Year of Birth: {year_of_birth}
#     Favorite Programming Language: {favorite_programming_language}
#     User ID: {user_id}
#     """
#     print(registration_summary)

# # 5. 
#     print("inittials: " + first_name[0].upper() + last_name[0].upper())
#     print("length of full name: " + str(len((first_name+last_name).replace(" ", ""))))

# # 6.

#     gender = int(input("Enter your gender (M/F) (1/0): ").strip())
#     like_programming  = bool(input("Do you like programming? (True/False): ").strip())

# ConsoleProgram()


# Part F - Stretch challenges Python Foundation
# 1. Seconds to hours, minutes, seconds
# total_seconds = int(input("Total seconds: "))
# hours = total_seconds // 3600
# minutes = (total_seconds % 3600) // 60
# seconds = total_seconds % 60

# print(f"{hours} hours, {minutes} minutes, {seconds} seconds")

# # tex 3700
# # 1 hour
# # 100 genom 60 --> 1 minute
# # 40 sekunder

# # 2.

# num = int(input("Enter a number 4 digits: "))

# print(f"First digit: {num // 1000}")
# print(f"Second digit: {(num // 100) % 10}")
# print(f"Third digit: {(num // 10) % 10}")
# print(f"Fourth digit: {num % 10}")

# # 3.
# word = input("Enter a word: ")
# print(f"Masked word: {word[:2]}*{word[-2:]}")

# 4.
# a) a = "abcde"
#    What is a[:: -1]
#            a[:: 2]
# b) bool(1)

# c) bool([])

# d) bool("")

# e) bool("False")

