'''
Prints data about each restaurant
'''
def runStat(dashes):
    restaurants = {}
    for dash in dashes.dashes:
        for restaurant in dash.deliveries:
            if restaurant.restaurant in restaurants:
                restaurants[restaurant.restaurant]["pay"] += restaurant.pay
                restaurants[restaurant.restaurant]["num"] += 1
            else:
                restaurants[restaurant.restaurant] = {"pay": restaurant.pay, "num": 1}

    for restaurant in sorted(restaurants.items(), key=lambda x: x[1]["num"]):
        print(restaurant[0])
        print("Deliveries:  " + str(restaurant[1]["num"]))
        print("Total pay:   $" + ("%.2f" % (restaurant[1]["pay"] / 100.)))
        print("Average pay: $" + ("%.2f" % ((restaurant[1]["pay"] / 100.) / restaurant[1]["num"])))
        print()

def getName():
    return "Restaurant statistics"