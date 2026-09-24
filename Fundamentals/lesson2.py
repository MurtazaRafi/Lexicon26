# THE LESSON 

# matrix_like = [
#     [1, 2, 3], 
#     [4, 5, 6], 
#     [7, 8, 9]
#     ]

# print(matrix_like[1][1])

# # Första 1:an säger access andra listan [4, 5, 6] och andra innuti [4,5,6], 5:an
# # Så för en matris --> första rad och andra kolumn 

# languages = ["Python", "Java", "C#"]

# languages.insert(1, "C++")
# print(languages)

# removed_language = languages.pop(-2)
# print(languages)
# print(f"Removed language: {removed_language}")

# # sort vs sorted

# # sorted för att returnera en ny sorterad lista utan att ändra den ursprungliga listan


# coordinates = (10, 20)

# # coordinates[0] = 15    
# # Python not compiled language

# x, y = coordinates

# print(f"x: {x}, y: {y}")

# # Man behöver ej temporary variable när switcha
# # Tex
# a = 5
# b = 10
# a, b = b, a
# print(f"a: {a}, b: {b}")


# # Set (ej dictionary)
# numbers = {1, 2, 3, 4}
# print(numbers)

# numbers = {1, 2, 2, 2, 3, 4, 4, 4}
# print(numbers) # Unika värden bara (en gång bara)

# users = ["anna", "bob" "anna"]
# unique_users = set(users)

# print(unique_users)
# # print(unique_users[0]) Går ej!

# # Set operations

# backend_languages = {"Python", "Java", "C#"}
# data_languages = {"Python", "R", "Julia"}

# print(backend_languages & data_languages)  # intersection (att båda har)
# print(backend_languages | data_languages)  # union ()
# print(backend_languages - data_languages)  # Difference: Removes only python from be_languages

# empty_collection = {}
# print(type(empty_collection)) # --> a dictionary, ej set


# # Dictionaries

# dic2 = {"name": "Anna", "score": "80"}
# print(dic2.keys())
# print(dic2.values())
# print(dic2.items())

# dic = [{"name": "Anna", "score": 80}, {"name": "Anna2", "score": 85}]

# print(dic[1]["score"])

# THE EXERCISES

# part A lists
# 1.
# 2.
# 3.
lst = ["a", "b", "c"]
lst.append("e")
print(lst)
lst.insert(-1, "d")
print(lst)
lst.remove("b")
end = lst.pop()

# 4.
# nums = [1,2,3,4,5]
# 
# 5. sort affects the original array/list
# nums.sort(reverse=True)
# print(nums)

list_a = [10,2,40]
# list_b = list_a 
# list_b.append(100)
# print(list_a)

# 6.
#fix
list_b = list_a.copy()

list_b.append(1000)

print(list_a)
print(list_b)

# part B tuples and unpacking
# 1.
rgb = (100, 100 , 100)
red, green, blue = rgb
print(red)
print(green)
# 2.
# 3. For fixed values. Constants

# tup = (1,2,3)
# tup[0] = 2 # Går ej

# 4.
cords = [(1,2),(3,4),(5,6),(7,8)]
print(cords[1])
print(cords[1][0])
print(cords[1][1])

# part C sets
# 1.
courses = ["pyt", "matlab", "pyt"]
print(len(set(courses)))

# 2.
set1 = {"a","b","c"}
set2 = {"a","e","d"}

print("share: " + str(set1 & set2))
print("only first has: "+ str(set1 - set2))
print("either person: "+ str(set1 | set2))

# 3.
set1.remove("a")
# 4. To remove dupplocates and keep only unique values. For example a set for unique keys of a certain data

# part D Dictionaries
# 1-4
laptop = {"brand": "HP", "model": "123", "RAM": 1000, "storage": "1GB", "price": 2000}
laptop["price"] = 3000
laptop["OS"] = "windows"

print(laptop.get("brand"))
print(laptop.get("brandee"))

print(laptop.keys())
print(laptop.values())
print(laptop.items())

# 5.
courses= {"C#": 100, "Java": 120, "Python": 130, "Erlang": 200}

print(sum(courses.values()))

# part E -nested colls
# 1.
books = [{"title": "Sagan om ringen", "author": "Gandalf", "pages": 100, "available": True},
 {"title": "Sagan om ringen 2", "author": "Gandalf", "pages": 150, "available": True},
 {"title": "Sagan om ringen3", "author": "Gandalf 3", "pages": 200, "available": False},
 {"title": "Sagan om ringen 4 ", "author": "Gandalf 4", "pages": 300, "available": True},
 {"title": "Sagan om ringen 5", "author": "Gandalf 5", "pages": 500, "available": False},
 ]
# 2.
print(books[2]["title"])
print(books[-1]["available"])
# 3.
books[0]["title"] = "Sagan om ringen 1"
books[0]["new key"] = "Iam a key"
print(books)
# 4.
departments = {"department1": ["Volvo", "Saab", "Scania"], "department2": ["VW", "Toyota", "Atlas Copco"]}
print(departments["department1"][2])
# 5.
courses2 = [{"name": "mixed", "teacher": "Murtaza", "topics": ["civil engineering", "dentist", "farmer"]},
            {"name": "mixed2", "teacher": "Murtaza2", "topics": ["civil engineering2", "dentist2", "farmer2", "Physician"]},
            {"name": "mixed3", "teacher": "Murtaza3", "topics": ["civil engineering 3", "dentist3", "farmer3"]}]

print(courses2[1]["topics"][-1])

# Part F applied challange: personal media catalogue
# 1. 2.
catalogue = [{"c_type": "movie", "year": 2016, "title": "movie 1", "avialable": False},
             {"c_type": "book", "year": 2019, "title": "book 1", "avialable": False},
             {"c_type": "movie", "year": 2025, "title": "movie 2", "avialable": True},
             {"c_type": "movie", "year": 2016, "title": "movie 3", "avialable": True},
             {"c_type": "game", "year": 2025, "title": "game 1", "avialable": True},
             {"c_type": "game", "year": 2025, "title": "game 2", "avialable": True},
             {"c_type": "movie", "year": 2016, "title": "movie 3b", "avialable": False},
             {"c_type": "movie", "year": 2016, "title": "movie 4", "avialable": False}]
             
# 3.
# Få movie book game
# print(set([c_type in for c_type in catalogue[:]["c_type"]]))
print({item["c_type"] for item in catalogue})

# 4.
# 5.
# 6.

# Part G - strech challenges
# 1.
# usernames1 = ["a", "b", "c"]
# usernames2 = ["f","d","a"]

# duplicates = set(usernames1) & set(usernames2)
# uniques = set(usernames1) | set(usernames2)

# print(duplicates)
# print(uniques)