# LAB 5
# Part A - Scope 
# 1.

course_name = "Python"

def my_courses():
    course_name = "C#"
    print("I love", course_name)

my_courses()
print("I don't like", course_name)

# "C#" is in a local scope (doesnt affect "Python")

# 2.

def count():
    counter = 0
# counter - unavailable

# 3.

# total = 100
# def add_tax():
#     total = total * 1.25
#     return total
# print(add_tax())

# The problem is total after the equal sign is not defined in that local scope
# Fix
total = 100
def add_tax(total):
    total = total * 1.25
    return total
print(add_tax(total))
# 4.
def func1():
    variabel1 = "var 1"
    def func2():
        variabel2 = "var 2"
        print(variabel1) #2
        print(variabel2) #3
    print(variabel1) #1
    func2()
func1()
# 1) func1 körs 2) func 2 körs

# 5
# def list(lst):
#     print(lst)

# list([1,2,3])

# part B - *args
# 1.
def add_all(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(add_all(1,2,3)) 

# 2.
def average(*numbers):
    if numbers is None:
        return 0
    return sum(numbers) / len(numbers)
print(average(1,2,3))

# 3.
def get_longest_word(*words):
    longest_word = ""
    length = 0 
    for word in words:
        if len(word) >= length:
            length = len(word)
            longest_word = word

    return longest_word
print(get_longest_word("Hej", "Hallå"))

# 4. 
def build_sentence(separator, *words):
    sentence = ""
    for word in words:
        sentence += word + separator
    return sentence

result = build_sentence("-", "Hej", "jag", "heter", "abcd")
print(result)

# 5. 
def describe_Score(student_name, *scores):
    total = 0
    count = 0

    for score in scores:
        total += score
        count += 1    
    return student_name, count, total/count

res = describe_Score("Murtaza", 100, 80, 70, 40)
print(res)

# part C - Positional unpacking
# 1. 

def three_parameter_function(*args):
    data1, data2, data3 = args
    print(data1)
    print(data2)
    print(data3)

lst = [10, 20, 30]
three_parameter_function(*lst)

# 2.
first_name = "Murtaza"
last_name = "Rafi"
city = "Stockholm"
tuple = (first_name, last_name, city)
def introduce(*tuple):
    for element in tuple:
        print(element, "-")
introduce(*tuple) # OBS *tuple och ej bara tuple

# 3.
def example(first, *middle, last = [8, 9, 10]):
    print(first)
    print(middle)
    print(last)
lst =  [3,4,5,6,7]
example("Murtaza", lst, last = [100, 200] )

# 4.
# In the function it means it can take x number of parameters
# When calling it means to unpack it to several arguments 

# part D - **kwargs
# 1.
def show_profile(**info):
    for key, value in info.items():
        print(key, value)

show_profile(name = "Murtaza", age =  33, status = True)
# 2.
def create_user(username, **details):
    dic = {}
    dic["username"] = username

    for key, value in details.items():
        dic[key] = value
    return dic
print(create_user("Murtaza", age =  33, status = True))
# 3.
def build_product(name, price, **metadata):
    dic = {}
    dic["name"] = name
    dic["price"] = price
    for key, data in metadata.items():
        dic[key] = data
    return dic
print(build_product("Murtaza", 500, status = True, is_active = True))

# 4.
def configure(**settings):
    dic = {}
    for key, value in settings.items():
        if settings[key] is not None:
            dic[key] = value

    return dic


print(configure(default = True, color = None, background = "white"))

# 5.
def show_information(**kwargs):
    for key, value in kwargs.items():
        print(key,":", value)

print(show_information(name = "Adam", age = 33, city = "Stockholm", language = "english"))

# part E - Combining parameters
# 1.
def log_event(event_type, *messages, **metadata):
    dic = {}
    dic["event_type"] = event_type

    i = 0
    for message in messages:
        dic["message " + str(i)] = message
        i = i + 1 

    for key, val in metadata.items():
        dic[key] = val

    return dic

message1 = "Hello"
message2 = "World"
log = log_event("Warning", message1, message2, data1 = "meta data 1", data2 = "meta data 2")
print(log)

# 2.
def calculate_order(customer, *prices, **options):
    total = 0
    for price in prices:
        print(price)
        total += price
    return total * options.get("discount") + options.get("shipping_fee")

customer = "Volvo"
prices = [1e6, 2e6,3e6]
options = {"discount": 0.5, "shipping_fee": 5e6}

print(calculate_order(customer, *prices, **options))

# 3.

# 4.

# Part F - Applied challange: Report Builder
# 1.
def create_report(title, *sections, **metadata):
    dic = {}

    dic["title"] = title

    i = 1
    j = 1
    for section in sections:
         if isinstance(section, str):
            dic["section " + str(i)] = section
            i += 1
         elif isinstance(section, dict):
             dic["teacher " + str(j)] = section.get("teacher " + str(j))
             j += 1

    for key, val in metadata.items():
        dic[key] = val

    return dic

# each section a string or dictionary
department = "Physics"
teacher1 = {"teacher 1": "Martin"}
teacher2 = {"teacher 2": "Maria"}

report = create_report("Information about department", department, teacher1, teacher2, course="Python")
print(report)

metadata = {"author" : "David", "department" : "R&D", "version" : 1.1, "confindential" : 2, "date" : "2026-09-18"}

report_2 = create_report("Information about department", department, teacher1, teacher2, **metadata)

print(report_2)

def summarize_report(report : dict):
    print(f"""summary: title: {report["title"]}""")
    for key, val in report.items():
        print(key, val)

summarize_report(report_2)

# 5
def count_words(*sections):
    words = 0
    for section in sections:
        if isinstance(section, str):
            words += len(section.split(" "))

    return words

print(count_words("Hej jag heter", 10, "vad heter du?"))
    

