# Lab 8
# Part A - Mutable default arguments

# 1.2.
class BadTeam:
    def __init__(self, name, members = []):
        self.name = name
        self.members = members
        
    def add_member(self, student):
        self.members.append(student)

bad_team_1 = BadTeam("Team A")
bad_team_2 = BadTeam("Team B")

bad_team_1.add_member("member 1")

print(bad_team_1.members)
print(bad_team_2.members)
# Both of them change. member 1 is added also to the second team - tillräcklig som svar?

# 3.4.
class Team:
    def __init__(self, name, members = None):
        self.name = name

        if members is None:
            members = []

        self.members = members
        
    def add_member(self, student):
        self.members.append(student)

team_1 = Team("Team A")
team_2 = Team("Team B")

team_1.add_member("member 1")

print(team_1.members)
print(team_2.members)

# Part B - Dictionary or class
# 1.
movie = {"title" : "Call of duty 4", "director" : "Charles", "rating": 5}

# 2. 3.
class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating
    def highly_rated(self):
        if self.rating >= 4:
            return True
        return False

movie2 = Movie("Call of duty 4", "Charles", 5)

# 4.
# For simple data representation with key-value pairs only I would use dictionary. But
# for more complex data representation with behaviour and many methods or when needing
# it for several places I'd use a class/object representation

# Part C - Inheritence fundamentals
# 1.
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
# 2. 
# class SavingAccount(Account):
#     def __init__(self, owner, balance, interest_rate):
#         self.owner = owner
#         self.balance = balance
#         self.interest_rate = interest_rate

class SavingAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

saving_account_1 = SavingAccount("Murtaza", 10000, 0)
saving_account_2 = SavingAccount("Karl", 20000, 0.01)

print(saving_account_1.owner, saving_account_1.balance)
print(saving_account_2.owner, saving_account_2.balance)

# Saving account "is a" Account --> makes sence to inherit from

# Part D - skipped

# Part E - super() and shared initialization
# 1.
# class Device:
#     def __init__(self, brand, year):
#         self.brand = brand
#         if year < 0:
#             raise ValueError("year cannot be negative!")
#         self.year = year
# 2.
class Device:
    def __init__(self, brand, year):
        self.brand = brand
        if year < 0:
            raise ValueError("year cannot be negative!")
        self.year = year
        self.is_active = True

# 3.
class Laptop(Device):
    def __init__(self, brand, year, ram_gb):
        super().__init__(brand, year)
        self.ram_gb = ram_gb
# 4.
class Mobile(Device):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model
# 5.
laptop = Laptop("HP", 2026, 100)
mobile = Mobile("Sony", 2020, "xyz")

print(laptop.is_active)
print(mobile.is_active)

# Part F - Method overriding

class Notification:
    def send(self):
        return "Your device needs attention!"

class EmailNotification(Notification):
    def send(Self):
        return super().send() + " Look at your email!"
class SMSNotification(Notification):
    def send(Self):
        return super().send() + " Check your phone!"

email_notification = EmailNotification()
sms_notification = SMSNotification()

print("notifications")
print(email_notification.send())
print(sms_notification.send())

# Part H - Applied challange: User accounts
class User:
    def __init__(self, username, email : str):
        self.username = username
        if email.isnumeric():
            raise ValueError("email can't be all numbers!")
        self.email = email
    def get_username(self):
        return self.username
    def get_role(self):
        return "general "
class AdminUser(User):
    def __init__(self, username, email):
        super().__init__(username, email)
    def get_role(self):
        return "admin"
    def get_email(self):
        return self.email
class PremiumUser(User):
    def __init__(self, username, email):
        super().__init__(username, email)
    def get_role(self):
        return super().get_role() + "+ premium"

# Inherited method
admin_user = AdminUser("Murtazar", "murtaza.rafi@gmail.com")
print(admin_user.get_username())
# Sub class method
admin_user = AdminUser("Ada", "ada.bolt@gmail.com")
print(admin_user.get_email())
# Overriden method
admin_user = PremiumUser("Kalle", "kalle.karlsson@gmail.com")
print(admin_user.get_role())

# 9.
# print(AdminUser("123", "123"))

# 10. Because they are both a form of user. We can say AdminUser "is a" User
