'''
Contains information for a delivery, including:
restaurant- the restaurant name
pay- the money made from the restaurant(doesn't include bonus if there was one)
'''
class Delivery:
    def __init__(self, restaurant, basePay, tip, startTime, endTime):
        self.restaurant = restaurant
        self.basePay = basePay
        self.tip = tip
        self.startTime = startTime
        self.endTime = endTime
