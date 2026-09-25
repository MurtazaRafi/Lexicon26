
from Room import Room

class Floor:
    def __init__(self, floor_number, rooms = None):
        self.floor_number = floor_number
        if rooms is None:
            self.rooms = []
        self.rooms = rooms
    def add_room(self, room):
        if room in self.rooms:
            raise ValueError("Room is already occupied!")
        self.rooms.append(room)
    def __str__(self):
        return self.floor_number
    def get_status(self):   
        return f"Occupied rooms: {", ".join([str(room.room_number) for room in self.rooms])}"