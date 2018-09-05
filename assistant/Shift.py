from assistant.Delivery import Delivery
from datetime import datetime

"""
Contains data for a single shift. Fields included are:
start: timestamp of when it began
end: timestamp of when it ended
region: the region the dash was worked in
total: total pay for the dash
additional: additional pay for the dash
deliveries: array of deliveries made in the dash
"""
class Shift:
    def __init__(self, start, end, region, additional, deliveries):
        self.start = start
        self.end = end
        self.region = region
        self.additional = additional
        self.deliveries = deliveries
        self.total = 0

    def __init__(self, start, end, region, additional):
        self.start = start
        self.end = end
        self.region = region
        self.additional = additional
        self.deliveries = []

    def addDelivery(self, restaurant, basePay, tip, startTime, endTime):
        self.deliveries.append(Delivery(restaurant, basePay, tip, startTime, endTime))
        self.total += basePay + tip


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
            d.print()
            print(("{:" + str(length + 2) + "}").format(d.restaurant) + "${:,.2f}".format((d.basePay + d.tip) / 100.))
