from Building import Building
from Floor import Floor
from Room import Room


class Address:
    def __init__(self, building : Building, address_ID, floor : Floor, room : Room):
        self.address_ID = address_ID
        self.building = building
        self.floor = floor
        self.room = room
    def __str__(self):
        return f"{self.building}, Floor number: {self.floor}, room number: {self.room}"
    def get_building_info(self):
        output = f"Occupied floors at building {self.building}: "

        for floor in self.building.floors:
            output += str(floor.floor_number) + " "

        output += f"\nOccupied rooms at floor number {self.floor.floor_number}: "

        for room in self.floor.rooms:
            output += str(room.room_number) + " "

        return output
