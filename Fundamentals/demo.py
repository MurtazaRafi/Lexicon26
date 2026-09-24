# number = 10
# print(type(number))

# number = 10.5
# print(type(number))

# number = "ten"
# print(type(number))

# # Python is dynamically typed.


# isHere = True
# print(type(isHere)) # <class 'bool'>

# print(5 ** 2) # 5 raised to the power of 2

# print(5 // 2) # Floor division (returns int)

# bool(1) # True

# bool([]) # False

# bool("") # False

# name = "John"
# age = 30

# print(f"My name is {name} and I am {age} years old.") # f-string formatting


# language = "Python"
# print(len(language)) # Length of the string

# text  = "Python"
# print(text[0]) # Accessing first character

# print(text[-1]) # Accessing last character

# print(text[-2]) # Accessing second last character

# text = "Python"
# print(text[0:2]) # Accessing first two characters

# Slicing with step
text = "abcdefghij"
print(text[::2])

# Reverese
print(text[::-1])

# Strings are immutable in Python. You cannot change a character in a string directly.

# word = "Python"
# word[0] = "J" # This will raise an error

# print(word) 

word = "Python"
word = "J" + word[1:] # This creates a new string
print(word) # Output: Jython
# Skapar en ny sträng + lägger till förra ordet till den  

# String Methods

# message = "  Hello Python  "

# print(message.lower())
# print(message.upper())
# print(message.strip())

# message = "Python is fun"
# print(message.replace("fun", "powerful"))

data = "apple, bananana, orange"
print(data.split(", "))