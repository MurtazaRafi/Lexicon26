from Floor import Floor

class Building:
    def __init__(self, address, floors = None):
        self.address = address
        if floors is None:
            self.floors = []
        else:
            self.floors = floors
        self.MAX_FLOORS = 10
    def add_floor(self, floor):
        if len(self.floors) >= self.MAX_FLOORS:
            raise ValueError("Maximum number of floors reached!")
        self.floors.append(floor)
    # def add_floor2(self, floor_number):
    #     for f in self.floors:
    #         if(floor_number == f.floor_number):
    #             raise ValueError("Room is already occupied!")
    #     floor = Floor(floor_number)
    #     self.floors.append(floor_number)
    def __str__(self):
        return self.address
    def get_status(self):
        return f"Occupied floors at building {self.address}: {", ".join([str(floor.floor_number) for floor in self.floors])}"