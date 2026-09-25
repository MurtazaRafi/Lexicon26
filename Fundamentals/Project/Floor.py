
from Room import Room

class Floor:
    def __init__(self, rooms = None):
        if rooms is None:
            self.rooms = []
        self.rooms = rooms
    def add_room(self, room):
        self.rooms = self.rooms.append(room)