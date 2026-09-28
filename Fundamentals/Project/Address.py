class Address:
    def __init__(self, building, floor, room):
        self.building = building
        self.floor = floor
        self.room = room
    def __str__(self):
        return f"{self.building}, Floor number: {self.floor}, room number: {self.room}"