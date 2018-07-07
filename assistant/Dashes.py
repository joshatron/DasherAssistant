'''
Contains array of dashes
'''
class Dashes:
    def __init__(self):
        self.dashes = []
        self.restaurants = set()
        self.regions = set()

    def addDash(self, dash):
        self.dashes.append(dash)
        for delivery in dash.deliveries:
            self.restaurants.add(delivery.restaurant)
        self.regions.add(dash.region)
