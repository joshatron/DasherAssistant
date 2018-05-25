'''
Prints general statistics from all dashes
'''
def runStat(dashes):
    totalMoney = 0
    totalHours = 0.0
    totalDashes = 0
    totalDeliveries = 0
    for dash in dashes.dashes:
        totalMoney += dash.total
        delta = dash.end - dash.start
        totalHours += (delta.seconds / 60.) / 60.
        totalDashes += 1
        totalDeliveries += len(dash.deliveries)

    print("Total dashes done: " + str(totalDashes))
    print("Total deliveries made: " + str(totalDeliveries))
    print("Total money made: $" + ("%.2f" % (totalMoney / 100.)))
    print("Total hours worked: " + str(int(totalHours)))
    print("Overall average hourly rate: $" + ("%.2f" % (int(totalMoney / totalHours) / 100.)))
    print("Overall average deliveries per hour: " + ("%.2f" % (totalDeliveries / totalHours)))
    print()

def getName():
    return "General overall stats"