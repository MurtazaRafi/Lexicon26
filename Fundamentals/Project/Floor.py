
from Room import Room

class Floor:
    def __init__(self, floor_number, rooms = None ):
        self.floor_number = floor_number
        if rooms is None:
            self.rooms = []
        self.rooms = rooms
    def add_room(self, room):
        self.rooms = self.rooms.append(room)
    def get_status(self):
        return self.rooms
    def __str__(self):
        return self.floor_number
        # for room in self.rooms:
        #     print(room.room_number)
    def get_status(self):   
        return f"Occupied rooms: {[room.room_number for room in self.rooms]}"