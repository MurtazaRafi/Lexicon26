# Gör den här filen till en read me
# Om att det här är en project om "hotel booknings system" i python.
# This file works as a booking manager. Handles the bookings and interaction of the entities between eachother
from sqlite3 import Date

from Customer import Customer
from Booking import Booking
from Address import Address
from Room import Room
from Building import Building
from Floor import Floor
from Room import Room


# # Create data
# room = Room(room_number=2)
# # print(room.room_number)
# floor = Floor(floor_number=3) # Ej rätt ! room kan läggas till
# building = Building("Götgatan 2", floors=[floor])
# customer = Customer(1, "Murtaza Rafi", 33)
# booking1 = Booking(booking_ID=1, created_at_date="2026-09-25:22:30", from_date="2026-09-25:00:00", to_date="2026-09-27:00:00", customer=customer, room=room)

# print(booking1)

# # Get stutus of the building and the floor
# print(building.get_status())
# print(floor.get_status())

# Create 100 free spaces in one building contianing 10 floors each containing 10 rooms - genom att ha/Sätta MAX_ROOMS = 10 i classen ??


# How can I check (without considering the dates) if one room is full or not?

# # create some more rooms in this floor
# room2 = Room(room_number=4)
# room3 = Room(room_number=5)
# floor.add_room(room=room2)
# room2.occupy()
# floor.add_room(room=room3)
# room3.occupy()
# print(floor.get_status())

# not allow already taken
# floor.add_room(room=room3)

# generate 10 rooms with 10 room numbers (so that floor 3 becomes "full")

rooms = [{"room" : "room1", "room_number": 1}, {"room" : "room2", "room_number": 2}, {"room" : "room3", "room_number": 3},
         {"room" : "room4", "room_number": 4},{"room" : "room5", "room_number": 5},{"room" : "room6", "room_number": 6},
         {"room" : "room7", "room_number": 7},{"room" : "room8", "room_number": 8},{"room" : "room9", "room_number": 9},{"room" : "room10", "room_number": 10}]

# TODO kan ha denna logik innuti floor och samma med buidling
floor3 = Floor(floor_number=3) # Ej rätt ! room kan läggas till
for room in rooms:
    room["room"] = Room(room["room_number"])
    room["room"].occupy()
    floor3.add_room(room=room["room"])
print(rooms[0]["room"])

# Try to add another room and duplicate room in floor 3

# room11 = Room(1)
# floor3.add_room(room11)

# Remove one room from floor3
floor3.remove_room(rooms[0]["room"])
rooms[0]["room"].vacate()

building1 = Building("Hagavägen 1")
building1.add_floor(floor=floor3)

print(building1.get_status())
print(floor3.get_status())

customer1 = Customer(100, "Murtaza rafi", 33)
address1 = Address(building1, floor3, room=rooms[3]["room"])



booking1 = Booking(1, "2026-09-28:9:30", "2026-09-28:00:00", "2026-09-29:00:00", customer1, address1)
# TODO Bryt ut till metoder/funktioner
print(booking1)

# TODO Lägg till fler data med for loops + fixa while loop för vad man vill göra med menyer med inmatning input()

room11 = Room(10, 2000, True)
floor5 = Floor(5, [room11])
building1.add_floor(floor5)

print(building1.get_status())
print(floor3.get_status())
print(floor5.get_status())



start_date = "2026-09-28"
# TODO extra funtkiolitet i mån av tid !

# add depending on the dates
# om det sepcifika rummet ej bokat under den tiden
#
#