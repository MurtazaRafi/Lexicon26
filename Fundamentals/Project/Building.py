
class Building:

    def __init__(self, address, floors = None):
        self.address = address
        if floors is None:
            self.floors = []
        self.floors = floors
    def add_floor(self, floor):
        self.floors = self.floors.append(floor)
    def get_status(self):
        return f"Occupied floors: {[floor.floor_number for floor in self.floors]}"
