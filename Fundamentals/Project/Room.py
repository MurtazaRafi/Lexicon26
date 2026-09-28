class Room:
    def __init__(self, room_number, price = 1000, occupied = False):
        self.room_number = room_number
        self.occupied = occupied
        self.price = price
    def __str__(self):
        return str(self.room_number)
    def occupy(self):
        if self.occupied:
            raise ValueError("Room already occupied!")
        self.occupied = True
    def vacate(self):
        if not self.occupied:
            raise ValueError("No such room!")
        self.occupied = False
            