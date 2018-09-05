'''
Contains array of dashes
'''
class Shifts:
    def __init__(self):
        self.shifts = []
        self.restaurants = set()
        self.regions = set()

    def addShifts(self, shift):
        self.shifts.append(shift)
        for delivery in shift.deliveries:
            self.restaurants.add(delivery.restaurant)
        self.regions.add(shift.region)
