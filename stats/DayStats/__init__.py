def runStat(dashes):
    dayPay = [0, 0, 0, 0, 0, 0, 0]
    dayDashes = [0, 0, 0, 0, 0, 0, 0]
    dayDeliveries = [0, 0, 0, 0, 0, 0, 0]
    dayTime = [0, 0, 0, 0, 0, 0, 0]
    dayStrings = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for dash in dashes.dashes:
        dayPay[dash.start.weekday()] += dash.total
        dayDashes[dash.start.weekday()] += 1
        dayDeliveries[dash.start.weekday()] += len(dash.deliveries)
        dayTime[dash.start.weekday()] += (((dash.end - dash.start).seconds / 60.) / 60.)

    for i in range(7):
        print(dayStrings[i])
        print("Total dashes done: " + str(dayDashes[i]))
        print("Total hours worked: " + str(int(dayTime[i])))
        print("Average pay rate: $" + ("%.2f" % (int(dayPay[i] / dayTime[i]) / 100.)))
        print("Average deliveries per hour: " + ("%.2f" % (dayDeliveries[i] / dayTime[i])))
        print()


def getName():
    return "Day statistics"
