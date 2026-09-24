# LAB 10
# Part A - Polymorphism

class EmailNotification:
    def send(self):
        return "notification from email"
class SMSNotification:
    def send(self):
        return "notification from SMS"
class PushNotification:
    def send(self):
        return "notification from push"

email_notification = EmailNotification()
sms_notification = SMSNotification()
push_notification = PushNotification()
notifications = [email_notification, sms_notification, push_notification]

for notificition in notifications:
    print(notificition.send())

# Part B - Polymorphism with inheritence

class Document:
    def __init__(self, title):
        self.title = title
    def describe(self):
        return "This is a document"
class PDFDocument(Document):
    def __init__(self, title):
        super().__init__(title)
    def describe(self):
        return "This is a PDF document"
class TextDocument(Document):
    def __init__(self, title):
        super().__init__(title)
    def describe(self):
        return "This is a text document"

pdf_doc1 = PDFDocument("pdf 1")
pdf_doc2 = PDFDocument("pdf 2")
text_doc1 = TextDocument("text 1")
text_doc2 = TextDocument("text 2")
documents = [pdf_doc1, text_doc2, text_doc1, pdf_doc2]
for doc in documents:
    print(doc.title, doc.describe())

# Part C - Duck Typing
# It works because Python allows duck typing. It means the objects are given more importance than the classes.
# The methods and the attributes only need to be the same and not their class types !

# Part D - isinstance()
class User:
    pass
class AdminUser(User):
    pass
admin_user = AdminUser()

print(isinstance(admin_user, AdminUser))
print(isinstance(admin_user, User))
print(isinstance(admin_user, str))
# 5.
# Because admin user inherits from user

# Part E - __str__
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name} - {self.price}"
product = Product("Laptop", 2000)
print(product)

product1 = Product("Laptop", 2000)
product2 = Product("Car", 5500)
product3 = Product("Airplane", 1000000)

print(product1)
print(product2)
print(product3)

p_str = str(product3)
print(type(p_str))

# Part F - __str__ with inheritence

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f"{self.owner} - {self.balance}"

class SavinAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    def __str__(self):
        return super().__str__() + f" - {self.interest_rate}"

account = Account("Dave", 1000)
saving_account = SavinAccount("Martin", 2000, 300)

print(account)
print(saving_account)

# Part G - Inheritence or composition?

class CPU:
    def __init__(self, model):
        self.model = model

class Computer:
    def __init__(self, brand, cpu):
        self.brand = brand
        self.cpu = cpu
cpu = CPU("Intel Core i5")
computer = Computer("Dell", cpu)

print(computer.brand, computer.cpu.model)

# 5. Because computer contains cpu

# 6. Car / Engine - a car has an engine
#    Manager / Employee - a manager is an empoyee
#    Course / Teacher - a course has a teacher
#    Phone / Device - a Phone is a Device

# Part H - Applied challange: Export system
class Exporter:
    def export(self, data):
        self.data = data
        return data
class ConsoleExporter(Exporter):
    def export(self, data):
        self.data = data
        return "Console: " + data
    def __str__(self):
        return self.export(self.data)
class TextExporter(Exporter):
    def export(self, data):
        self.data = data
        return "Text: " + data
    def __str__(self):
        return self.export(self.data)
class SummaryExporter(Exporter):
    def export(self, data):
        self.data = data
        return "Summary: " + data
    def __str__(self):
        return self.export(self.data)

console = ConsoleExporter()
# report1 = console.export("Customer report")
text = TextExporter()
# report2 = text.export("Manager report")
summary = SummaryExporter()
# report3 = summary.export("summary report")

reports = [console, text, summary]

for report in reports:
    print(report.export("Some file data"))

# 8
class Graph:
    def export(self, data):
        self.data = data
        return "Graph: " + data
    def __str__(self):
        return self.export(self.data)

graph = Graph()
new_list = [*reports, graph]


for report in new_list:
    print(report.export("Some file data"))

# 9
print(isinstance(console, Exporter))

# 10

class StapleDiagram:
    def __init__(self, title):
        self.title = title
    def __str__(self):
        return self.title

staple_diagram = StapleDiagram("Graph 1")

class Graph2:
    def export(self, data, staple_diagram):
        self.data = data
        self.staple_diagram = staple_diagram
        return "Graph: " + data
    def __str__(self):
        return self.export(self.data) 

graph2 = Graph2()
print(graph2.export("Some data", staple_diagram))
print(graph2.staple_diagram)
# Explanation: A graph can have different types of graphs, among others staple diagram
