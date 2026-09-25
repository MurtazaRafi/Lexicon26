# Gör den här filen till en read me
# Om att det här är en project om "hotel booknings system" i python.
# This file works as a booking manager. Handles the bookings and interaction of the entities between eachother
from Customer import Customer
from Booking import Booking
from Room import Room
from Building import Building
from Floor import Floor
from Room import Room


# Create data
room = Room(room_number=2)
print(room.room_number)
floor = Floor(floor_number=1, rooms=[room])
building = Building("Götgatan 2", floors=[floor])
customer = Customer(1, "Murtaza Rafi", 33)
booking1 = Booking(booking_ID=1, created_at_date="2026-09-25:22:30", from_date="2026-09-25:00:00", to_date="2026-09-27:00:00", customer=customer, room=room)

print(booking1)

# Get stutus of the building and the floor
print(building.get_status())
print(floor.get_status())

# Create 100 free spaces in one building contianing 10 floors each containing 10 rooms - genom att ha/Sätta MAX_ROOMS = 10 i classen ??


# How can I check (without considering the dates) if one room is full or not?

#floor.add_room(room=room)

# create some more rooms in this floor


