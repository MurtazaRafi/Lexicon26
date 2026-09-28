
class Building:
    def __init__(self, address, floors = None):
        self.address = address
        if floors is None:
            self.floors = []
        self.floors = floors
        self.MAX_FLOORS = 10
    def add_floor(self, floor):
        if len(self.floors) >= self.MAX_FLOORS:
            raise ValueError("Maximum number of floors reached!")
        self.floors = self.floors.append(floor)
    def get_status(self):
        return f"Occupied floors: {", ".join([str(floor.floor_number) for floor in self.floors])}"
