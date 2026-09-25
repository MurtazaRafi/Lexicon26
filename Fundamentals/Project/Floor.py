
from Room import Room

class Floor:
    def __init__(self, floor_number, rooms = None):
        self.floor_number = floor_number
        if rooms is None:
            self.rooms = []
        self.rooms = rooms
    def add_room(self, room):
        self.rooms = self.rooms.append(room)