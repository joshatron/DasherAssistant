def runStat(dashes):
    restaurants = {}
    for dash in dashes.dashes:
        for restaurant in dash.deliveries:
            if restaurant.restaurant in restaurants:
                restaurants[restaurant.restaurant]["pay"] += restaurant.pay
                restaurants[restaurant.restaurant]["num"] += 1
            else:
                restaurants[restaurant.restaurant] = {"pay": restaurant.pay, "num": 1}

    for restaurant in restaurants:
        print(restaurant)
        print("Deliveries:  " + str(restaurants[restaurant]["num"]))
        print("Total pay:   $" + ("%.2f" % (restaurants[restaurant]["pay"] / 100.)))
        print("Average pay: $" + ("%.2f" % ((restaurants[restaurant]["pay"] / 100.) / restaurants[restaurant]["num"])))
        print()

def getName():
    return "Restaurant statistics"