def runStat(dashes):
    days = [[{"rate": 0, "num": 0} for col in range(24)] for row in range(7)]

    for dash in dashes.dashes:
        rate = dash.total / (((dash.end - dash.start).seconds / 60.) / 60.)
        start = dash.start.hour
        if(dash.start.minute > 29):
            start += 1
        end = dash.end.hour
        if(dash.end.minute > 29):
            end += 1
        # doesn't handle dash that goes past midnight well
        for i in range(start, end):
            days[dash.start.weekday()][i]["rate"] += rate
            days[dash.start.weekday()][i]["num"] += 1

    dayStrings = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Day |00:00 |01:00 |02:00 |03:00 |04:00 |05:00 |06:00 |07:00 |08:00 |09:00 |10:00 |11:00 |12:00 |13:00 |14:00 |15:00 |16:00 |17:00 |18:00 |19:00 |20:00 |21:00 |22:00 |23:00 |")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for i in range(7):
        dayString = dayStrings[i] + " |"
        for hour in days[i]:
            if hour["num"] != 0:
                dayString += "$" + "%.2f" % (int(hour["rate"] / hour["num"]) / 100.) + "|"
            else:
                dayString += "      |"
        print(dayString)
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

def getName():
    return "Time and day statistics"