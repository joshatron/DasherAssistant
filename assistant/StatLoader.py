import imp
import os

def findStats():
    stats = []
    statsList = os.listdir("./stats")
    for file in statsList:
        if not os.path.isdir("./stats/" + file) or not "__init__.py" in os.listdir("./stats/" + file):
            continue
        info = imp.find_module("__init__", ["./stats/" + file])
        tempStat = imp.load_module("__init__", *info)
        stats.append({"name": tempStat.getName(), "info": info})

    return stats

def loadStat(stat):
    return imp.load_module("__init__", *stat["info"])
