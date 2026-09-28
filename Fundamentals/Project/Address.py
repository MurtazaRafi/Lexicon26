class Address:
    def __init__(self, building, floor, room):
        self.building = building
        self.floor = floor
        self.room = room
    def __str__(self):
        return f"{self.building}, Floor number: {self.floor}, room number: {self.room}"
#     def __str__(self):
#         pass
#     def get_status(self):
#         pass
#     def 
# class Building:
#     def __init__(self, address, floors = None):
#         self.address = address
#         if floors is None:
#             self.floors = []
#         else:
#             self.floors = floors
#         self.MAX_FLOORS = 10
#     def add_floor(self, floor):
#         if len(self.floors) >= self.MAX_FLOORS:
#             raise ValueError("Maximum number of floors reached!")
#         self.floors.append(floor)
#     def get_status(self):
#         return f"Occupied floors at building {self.address}: {", ".join([str(floor.floor_number) for floor in self.floors])}"

# class Floor:
#     def __init__(self, floor_number, rooms = None):
#         self.floor_number = floor_number
#         if rooms is None:
#             self.rooms = []
#         else:
#             self.rooms = rooms
#         self.MAX_ROOMS = 10
#     def add_room(self, room):
#         if room in self.rooms:
#             raise ValueError("Room is already occupied!")
#         if len(self.rooms) >= self.MAX_ROOMS:
#             raise ValueError("Maximum number of rooms reached!")
#         self.rooms.append(room)
#         print(self.rooms)
#     def remove_room(self, room):
#             if room not in self.rooms:
#                 raise ValueError("Room does not exist in this floor!")
#             self.rooms.remove(room)
#     def __str__(self):
#         return self.floor_number
#     def get_status(self):   
#         return f"Occupied rooms at floor number {self.floor_number}: {", ".join([str(room.room_number) for room in self.rooms])}"

# class Room:
#     def __init__(self, room_number, price = 1000, occupied = False):
#         self.room_number = room_number
#         self.occupied = occupied
#         self.price = price
#     def __str__(self):
#         return str(self.room_number)
#     def occupy(self):
#         if self.occupied:
#             raise ValueError("Room already occupied!")
#         self.occupied = True
#     def vacate(self):
#         if not self.occupied:
#             raise ValueError("No such room!")
#         self.occupied = False
            