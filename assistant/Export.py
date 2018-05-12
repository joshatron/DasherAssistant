import json


def exportToFile(dashes, file):
    ds = []
    for dash in dashes.dashes:
        d = {}
        d["start"] = dash.start
        d["end"] = dash.end
        d["region"] = dash.region
        d["total"] = dash.total
        d["additional"] = dash.additional
        deliveries = []
        for delivery in dash.deliveries:
            deliveries.append({"restaurant": delivery.restaurant, "pay": delivery.pay})
        d["deliveries"] = deliveries
        ds.append(d)

    json_text = json.dumps(ds, indent=2)
    f = open(file, "w")
    f.write(json_text)
    f.close()
