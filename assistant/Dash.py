from assistant.Delivery import Delivery
from datetime import datetime

"""
Contains data for a single dash. Fields included are:
start: timestamp of when it began
end: timestamp of when it ended
region: the region the dash was worked in
total: total pay for the dash
additional: additional pay for the dash
deliveries: array of deliveries made in the dash
"""
class Dash:
    def __init__(self, start, end, region, total, additional, deliveries):
        self.start = start
        self.end = end
        self.region = region
        self.total = total
        self.additional = additional
        self.deliveries = deliveries

    def __init__(self, start, end, region, total, additional):
        self.start = start
        self.end = end
        self.region = region
        self.total = total
        self.additional = additional
        self.deliveries = []

    def addDelivery(self, restaurant, pay):
        self.deliveries.append(Delivery(restaurant, pay))

    def print(self):
        print("start: " + self.start.strftime("%m/%d/%y %H:%M"))
        print("end: " + self.end.strftime("%m/%d/%y %H:%M"))
        print("region: " + self.region)
        print("total pay: " + "${:,.2f}".format(self.total / 100.))
        print("additional pay: " + "${:,.2f}".format(self.additional / 100.))
        print("deliveries:")
        length = 0
        for d in self.deliveries:
            if(len(d.restaurant) > length):
                length = len(d.restaurant)
        for d in self.deliveries:
            print(("{:" + str(length + 2) + "}").format(d.restaurant) + "${:,.2f}".format(d.pay / 100.))
