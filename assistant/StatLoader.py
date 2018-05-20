import imp
import os

def loadStats():
    stats = []
    statsList = os.listdir("../stats")
    for file in statsList:
        if not os.path.isdir("../stats/" + file) or not "__init__.py" in os.listdir("../stats/" + file):
            continue
        info = imp.find_module("__init__", ["../stats/" + file])
        stats.append(imp.load_module("__init__", *info))

    return stats
