import json
from datetime import datetime

from assistant.Dash import Dash
from assistant.Dashes import Dashes


'''
Imports dash data from a json file
'''
def importJSON(file):
    jsonString = open(file).read()
    data = json.loads(jsonString)
    dashes = Dashes()
    for dash in data:
        d = Dash(datetime.strptime(dash["start"], "%m/%d/%y %H:%M"), datetime.strptime(dash["end"], "%m/%d/%y %H:%M"), dash["region"], dash["total"], dash["additional"])
        for delivery in dash["deliveries"]:
            d.addDelivery(delivery["restaurant"], delivery["pay"])
        dashes.addDash(d)
    return dashes

'''
Imports dash data from user input
'''
def importManual():
    start = 0
    while True:
        startStr = input("What is the start date and time (MM/DD/YY HH:MM)? ")
        try:
            start = datetime.strptime(startStr, "%m/%d/%y %H:%M")
            break;
        except:
            print("Invalid date. Please use specified format")

    end = 0
    while True:
        endStr = input("What is the end date and time (MM/DD/YY HH:MM)? ")
        try:
            end = datetime.strptime(endStr, "%m/%d/%y %H:%M")
            break;
        except:
            print("Invalid date. Please use specified format")

    region = input("What is the region? ")

    total = 0
    while True:
        totalStr = input("What was the total pay? $")
        try:
            total = int(float(totalStr) * 100)
            break
        except:
            print("Invalid input. Please enter a valid number")

    additional = 0
    while True:
        additionalStr = input("What was the additional pay? $")
        try:
            additional = int(float(totalStr) * 100)
            break
        except:
            print("Invalid input. Please enter a valid number")

    d = Dash(start, end, region, total, additional)
    print("Type the restaurant name and pay for each delivery.")
    print("Leave the restaurant blank to exit.")
    while True:
        restaurant = input("What was the restaurant name? ")
        if(restaurant != ""):
            pay = 0
            while True:
                payStr = input("What was the pay? $")
                try:
                    pay = int(float(payStr) * 100)
                    break
                except:
                    print("Invalid input. Please enter a valid number")

            d.addDelivery(restaurant, pay)
        else:
            break
    return d
