
from Room import Room

class Floor:
    def __init__(self, floor_number, rooms = None):
        self.floor_number = floor_number
        if rooms is None:
            self.rooms = []
        else:
            self.rooms = rooms
        self.MAX_ROOMS = 10
    def add_room(self, room):
        if room in self.rooms:
            raise ValueError("Room is already occupied!")
        if len(self.rooms) >= self.MAX_ROOMS:
            raise ValueError("Maximum number of rooms reached!")
        self.rooms.append(room)
        print(self.rooms)
    def remove_room(self, room):
            if room not in self.rooms:
                raise ValueError("Room does not exist in this floor!")
            self.rooms.remove(room)
    def __str__(self):
        return str(self.floor_number)
    def get_status(self):   
        return f"Occupied rooms at floor number {self.floor_number}: {", ".join([str(room.room_number) for room in self.rooms])}"