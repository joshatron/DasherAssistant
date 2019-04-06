'''
Contains information for a delivery, including:
restaurant- the restaurant name
pay- the money made from the restaurant(doesn't include bonus if there was one)
'''
class Delivery:
    def __init__(self, restaurant, pay):
        self.restaurant = restaurant
        self.pay = pay