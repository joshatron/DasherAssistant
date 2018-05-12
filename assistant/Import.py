import json

from assistant.Dash import Dash
from assistant.Dashes import Dashes


def importJSON(file):
    jsonString = open(file).read()
    data = json.loads(jsonString)
    dashes = Dashes()
    for dash in data:
        d = Dash(dash["start"], dash["end"], dash["region"], dash["total"], dash["additional"])
        for delivery in dash["deliveries"]:
            d.addDelivery(delivery["restaurant"], delivery["pay"])
        dashes.addDash(d)
    return dashes

def importManual():
    start = input("What is the start date and time (MM/DD/YYYY HH:MM:SS)? ")
    end = input("What is the end date and time (MM/DD/YYYY HH:MM:SS)? ")
    region = input("What is the region? ")
    total = int(float(input("What was the total pay? $")) * 100)
    additional = int(float(input("What was the additional pay? $")) * 100)
    d = Dash(start, end, region, total, additional)
    print("Type the restaurant name and pay for each delivery.")
    print("Leave the restaurant blank to exit.")
    while True:
        restaurant = input("What was the restaurant name? ")
        if(restaurant != ""):
            pay = int(float(input("What was the pay? $")) * 100)
            d.addDelivery(restaurant, pay)
        else:
            break
    return d
