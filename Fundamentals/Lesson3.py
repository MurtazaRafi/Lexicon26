# part A conditions
# 1.
# num = -1

# if num == 0:
#     print("zero")
# elif num > 0:
#     print("pos")
# else:
#     print("neg")
# # 2.
# # too easy

# # 3.
# username = "m"
# password = "p"

# if username == "m" and password == "p":
#     print("valid")
# else:
#     print("not val")
# # 4.
# score = 100

# if score <= 30:
#     print("F")
# elif score <= 50:
#     print("E")
# elif score <= 60:
#     print("D")
# elif score <= 70:
#     print("C")
# elif score <= 80:
#     print("B")
# else:
#     print("A")

# # 5.
# total_order = 4
# is_member = True
# if total_order >= 3 and is_member:
#     print("shipped")
# elif total_order < 3 or not is_member:
#     print("Not possible to ship")
# 6.

# part B - truthy, falsy and membership
# 1.
# [] 0 "" --> falsy
# s = 0
# if s:
#     print("kmklm")

# 2.

# 3. 4
# usernames = ["a", "b", "c"]
# username = "a"
# if username not in usernames:
#     print("ok")
# else:
#     print("blocked")

# # part c for loops
# # 1.
# names = ["Eva", "Adam", "Anna"]
# for name in names:
#     print("hello " + name)
# # 2.
# for num in range(1, 50):
#     if num % 2 == 0:
#         print(num)
# # 3.
# words = ["Hello", "How", "Are"]

# # 5.
# count = 0
# for word in words:
#     if len(word) >= 5:
#         count += 1
# print(count)

# # 6.

# # 7.
# dict = {"name": "Murtaza", "user": "username", "born": 1990}

# for key, value in dict.items():
#     print(key, value)

# # part d range, enumerate and nested loops
# # 1.
# for i in range(10,0,-1):
#     print(i)
# # 2.
# num = int(input("num")10)
# for i in range(1, 10):
#     print(num * i)
# 3.
# tracks = ["a", "b", "c"]
# for index, track in enumerate(tracks):
#     print(index, track)
# # 4.
# for i in range(3):
#     for j in range(4):
#         print("cords: ", (i, j))
# # 5.
# a = []
# for i in range(5):
#     temp = []
#     for j in range(5):
#         temp.append(j)
#     a.insert(i, temp)

# print(a)

# # Part E - while loops
# # 1.
# count = 10
# while count >= 0:
#     print(count)
#     count -= 1
# # 2.
# correct_password = "abc"
# given_password = ""
# while given_password != correct_password:
#     given_password = input("give a correct password")

# # 3.
# show = True
# user_input = ""
# while show and user_input != "quit":
#     print("pick a menu 1. 2. 3. or quit.")
#     user_input = input()
#     if user_input == "1":
#         print("menu 1")
#     elif user_input == "2":
#         print("menu 2")
#     elif user_input == "3":
#         print("menu 3")

# # 4.

# show = True
# user_input = ""
# while show and user_input != "quit":
#     print("pick a menu 1. 2. 3. or quit.")
#     user_input = input()
#     if user_input == "1":
#         print("menu 1")
#     elif user_input == "2":
#         print("menu 2")
#     elif user_input == "3":
#         print("menu 3")

# 5.

# def GuessNumber():
#     secret_number = 10
#     print("Guess the secret number")
#     user_number = int(input())
#     show = True
#     while user_number != secret_number:
#         if user_number == secret_number:
#             print("Perfect, you guessed it!")
#         elif user_number < secret_number:
#             print("less than the secret nr")
#             user_number = int(input())
#         else:
#             print("higher than the secret nr")
#             user_number = int(input())

# # GuessNumber()

# # part F break and continue
# # 1.
# for i in range(1, 100):
#     print(i)
#     if i % 7 == 0 and i % 9 == 0:
#         break
# # 2.
# lst = ["a", "b" , "c", ""]
# for element in lst:
#     if element:
#         print(element)
# 3.
# target_name = "Murtaza"
# lst = ["Murtza", "b" , "c", ""]
# for name in lst:
#     if name == target_name:
#         print("found")
#         break
# else:
#     print("didnt match")

# 4.
# if num > 0:
# if num == 999 break

# Part G Applied challange: console study tracker
# 1.
dic = [{"subject": "Python 1" , "minutes": 120},
       {"subject": "Python 2" , "minutes": 180},
       {"subject": "Python 3" , "minutes": 120},
       {"subject": "Python 1" , "minutes": 100},
       {"subject": "Python 2" , "minutes": 120},
       {"subject": "Python6 " , "minutes": 300},
       {"subject": "Python7" , "minutes": 120},
       {"subject": "Python8" , "minutes": 180},
       {"subject": "Pytho9" , "minutes": 200},
       {"subject": "Python 10" , "minutes": 120}] 
# 2.
# minutes = 0
# for i in range(len(dic)):
#     minutes += dic[i]["minutes"]

# print(minutes)
# 3.
total_minutes = {} 

for i in range(len(dic)):
    if dic[i]["subject"] not in total_minutes:
       total_minutes[dic[i]["subject"]] = dic[i]["minutes"] 
    else:
        total_minutes[dic[i]["subject"]] += dic[i]["minutes"]

print(total_minutes)

# 4.
longest_minutes = 0
for subject in total_minutes:
    if total_minutes[subject] > longest_minutes:
        longest_minutes = total_minutes[subject]
print("longest_minutes", longest_minutes)

# 5.
# 6.
# 7.
# Part H stretch challenges

# 2.

sentence = "hello"
vowels = "aoieu"
count = 0
for char in sentence:
    if char in vowels:
        count += 1
print("vowels ", count)

# 3. 
nums = [0, 1 ,1 ,3 ,4, 4, 4]
set1 = set()
set2 = set()
for num in nums:
    if num not in set1:
        set1.add(num)
    else:
        set2.add(num)
print(set2)

# 4
numbers2 = [3 , 5 , 2]
for number in numbers2:
    for _ in range(number):
        print("*",end="")
    print("", end = "\n")