
class Building:
    def __init__(self, floors = None):
        if floors is None:
            self.floors = []
        self.floors = floors
    def add_floor(self, floor):
        self.floors = self.floors.append(floor)