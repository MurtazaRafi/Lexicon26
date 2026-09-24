# Lab 7
# Classes and objects
# 1.
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
    

# book1 = Book("book 1", "author 1", 200)
# print("book:", book1.title, "author:", book1.author, "pages:", book1.pages)
# book2 = Book("book 2", "author 2", 100)
# print("book:", book2.title, "author:", book2.author, "pages:", book2.pages)
# book3 = Book("book 3", "author 3", 300)
# print("book:", book3.title, "author:", book3.author, "pages:", book3.pages)
# book4 = Book("book 4", "author 4", 400)
# print("book:", book4.title, "author:", book4.author, "pages:", book4.pages)

# 2.
# class Laptop:
#     def __init__(self, brand, model, ram_gb, price):
#         self.brand = brand
#         self.model = model
#         self.ram_gb = ram_gb
#         self.price = price

# laptop1 = Laptop("HP", "model100", 200, 10000)
# laptop2 = Laptop("ACER", "model123", 150, 5000)
# laptop3 = Laptop("BENQ", "model1321", 100, 8000)
# laptop1.price = 5000
# print("laptop: ", laptop1.brand + " " + laptop1.model, "memory: ", laptop1.ram_gb, "price: ", laptop1.price)
# # 3.
# laptop4 = Laptop("ACER", "model123", 150, 5000)
# laptop5 = Laptop("ACER", "model123", 150, 5000)
# print(laptop4 is laptop5)
# # 4.
# class Laptop2:
#     def __init__(self, brand, model, ram_gb = 100, price = 10000):
#         self.brand = brand
#         self.model = model
#         self.ram_gb = ram_gb
#         self.price = price
# # 5.
# laptop6 = Laptop2(brand="HP", model="model123", ram_gb=150, price=5000)
# print("laptop: ", laptop6.brand + " " + laptop6.model, "memory: ", laptop6.ram_gb, "price: ", laptop6.price)

# # Part B - Methods and state
# # 1.

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#     def is_long(self):
#         if self.pages > 300:
#             return True
#         return False

# book4 = Book("book 4", "author 4", 400)
# print(book4.is_long())

# # 2.
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
# # 3.
#     def withdraw(self, amount):
#         if self.balance - amount < 0:
#             raise ValueError("Your account balance is below zero!")
#         self.balance -= amount
# # 4. 
# class Task:
#     def __init__(self, title, completed = False):
#         self.title = title
#         self.completed = completed
#     def complete(self):
#         self.completed = True
#     def reopen(self):
#         self.completed = False
# # 5.
# task1 = Task("Task 1", False)
# task2 = Task("Task 2", False)
# task2.completed = True
# print(task1.completed)

# # Part C - Instance and class attributes
# # 1-6
# class Product:
#     tax_rate = 0.25
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def price_with_tax(self):
#         return self.price * (1 + self.tax_rate)

# product1 = Product("BMW", 200000)
# print("product: ", product1.name, "price", product1.price_with_tax())
# product2 = Product("Ducati", 400000)
# print("product: ", product2.name, "price", product2.price_with_tax())
# product3 = Product("Porsche", 300000)
# print("product: ", product3.name, "price", product3.price_with_tax())

# Product.tax_rate = 0.2
# print("product: ", product1.name, "price", product1.price_with_tax())

# product2.tax_rate = 0.1
# print("product: ", product2.name, "price", product2.price_with_tax())

# # Part D - Collections of objects
# # 1. 
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def get_status(self):
#         if self.score >= 70:
#             return "PASS"
#         return "FAIL"
    
# student1 = Student("Ada", 80)
# student2 = Student("Eva", 60)
# student3 = Student("Björn", 70)
# student4 = Student("Anna", 85)
# student5 = Student("Ida", 92)
# student6 = Student("Adam", 72)

# # 2.
# students = [student1, student2, student3, student4, student5, student6]
# # 3.
# for student in students:
#     print("name:", student.name, "score", student.score)

# # 5. 
# print("name", "status")
# for student in students:
#     print(student.name, student.get_status())

# # 6.
# passed = [student for student in students if student.get_status() == "PASS"]
# print(passed)

# Part E - Objects inside objects
# 1.
# class Teacher:
#     def __init__(self, name):
#         self.name = name
 
# # 2. 
# class Course:

#     def __init__(self, name, teacher):
#         self.name = name
#         self.teacher = teacher
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)
       
# class Student:
#     def __init__(self, name):
#         self.name = name
# 3.
# teacher = Teacher("Levander")

# course = Course("Python Advanced", teacher)
# # 4.
# print("course name:", course.name, "teacher name:", course.teacher.name)
# # 6.
# course.add_student(student1)
# course.add_student(student2)
# course.add_student(student3)

# # 7.
# for student in course.students:
#     print(student.name)

# Part F - Applied Challange: Course manager
# 1-10
class Teacher:
    def __init__(self, name):
        self.name = name 
class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def get_students_list(self):
        return self.students
    def get_passed_students(self):
        return [student for student in self.students if student.get_status() == "PASS"]
    # G2.
    def get_threshold_students(self, score):
        threshold_students = []
        for student in self.students:
            if student.score >= score:
                threshold_students.append(student)

        return threshold_students
                
       
class Student:
    SCORE_LIMIT = 100
    def __init__(self, name, score):
        self.name = name
        if score < 0:
            raise ValueError("Can't provide negative score!")
        self.score = score
    def get_status(self):
        if self.score >= 70:
            return "PASS"
        return "FAIL"
    # part G1.
    def update_student_score(self, score):
        if score > 100:
            raise ValueError(f"Can't be above {self.SCORE_LIMIT}")
        self.score = score
    

student1 = Student("Ada", 80)
student2 = Student("Eva", 60)
student3 = Student("Björn", 70)
student4 = Student("Anna", 85)
student5 = Student("Ida", 92)

teacher = Teacher("Levander")

course = Course("Python and AI", teacher)
course.add_student(student1)
course.add_student(student2)
course.add_student(student3)
course.add_student(student4)
course.add_student(student5)

print(f"""COURSE SUMMARY \ncourse name: {course.name}\nteacher: {course.teacher.name}
All students: {", ".join([student.name for student in course.get_students_list()])}
Passed students: {", ".join([student.name for student in course.get_passed_students()])}""")

# Part G - stretch challenges
# 1. 
print(student1.name, student1.score)
student1.update_student_score(50)
print(student1.name, student1.score)

# 2.
[print(student.name, student.score) for student in course.get_threshold_students(51)]

# 3.
course2 = Course("C#", "Dimitris")
print(course2.students)

# 4.
# For example a constant, since it should be a constant across all students. SCORE_LIMIT