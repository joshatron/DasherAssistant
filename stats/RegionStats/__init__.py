def runStat(dashes):
    regions = {}
    for dash in dashes.dashes:
        if dash.region in regions:
            regions[dash.region]["pay"] += dash.total
            regions[dash.region]["num"] += 1
            delta = dash.end - dash.start
            regions[dash.region]["hours"] += (delta.seconds / 60.) / 60.
            regions[dash.region]["deliveries"] += len(dash.deliveries)
        else:
            delta = dash.end - dash.start
            regions[dash.region] = {"pay": dash.total, "num": 1, "hours": ((delta.seconds / 60.) / 60.), "deliveries": len(dash.deliveries)}

    for region in regions:
        print("Region: " + region)
        print("Dashes done: " + str(regions[region]["num"]))
        print("Deliveries done: " + str(regions[region]["deliveries"]))
        print("Money made: $" + str(regions[region]["pay"] / 100.))
        print("Hours worked: " + str(int(regions[region]["hours"])))
        print("Average hourly rate: $" + str(int(regions[region]["pay"] / regions[region]["hours"]) / 100.))
        print()

def getName():
    return "Stats per region"