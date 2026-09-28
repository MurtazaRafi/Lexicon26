class Address:
    def __init__(self, building, address_ID, floor, room):
        self.address_ID = address_ID
        self.building = building
        self.floor = floor
        self.room = room
    def __str__(self):
        return f"{self.building}, Floor number: {self.floor}, room number: {self.room}"