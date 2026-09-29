
from Room import Room


class Floor:
    def __init__(self, floor_number, rooms = None):
        self.floor_number = floor_number
        if rooms is None:
            self.rooms = [] # Kolla igen om rätt syntax
        else:
            self.rooms = rooms
        self.MAX_ROOMS = 10
    def add_room(self, room):
        if room in self.rooms:
            raise ValueError("Room is already occupied!")
        if len(self.rooms) >= self.MAX_ROOMS:
            raise ValueError("Maximum number of rooms reached!")
        self.rooms.append(room)
    def add_room2(self, room_number):
            for r in self.rooms:
                if(room_number == r.room_number):
                    raise ValueError("Room is already occupied!")
            room = Room(room_number)
            self.rooms.append(room)
            room.occupy()
    def remove_room(self, room):
            if room not in self.rooms:
                raise ValueError("Room does not exist in this floor!")
            self.rooms.remove(room)
    def __str__(self):
        return str(self.floor_number)
    def get_status(self):   
        return f"Occupied rooms at floor number {self.floor_number}: {", ".join([str(room.room_number) for room in self.rooms])}"