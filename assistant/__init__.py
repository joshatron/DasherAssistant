from assistant.Export import exportToFile
from assistant.Import import importJSON, importManual
from assistant.StatLoader import loadStats

dashes = importJSON("dashes.json")
stats = loadStats()

while True:
    print("What would you like to do?")
    print("1) add dash")
    print("2) print dashes")
    print("3) export")
    print("4) run statistic")
    print("5) exit")
    choice = int(input("Please choose an option: "))

    if choice == 1:
        dashes.addDash(importManual())
    elif choice == 2:
        i = 1
        for dash in dashes.dashes:
            print("Dash " + str(i))
            dash.print()
            print()
            i += 1
    elif choice == 3:
        exportToFile(dashes, "dashes.json")
    elif choice == 4:
        print("Choose a statistic to run")
        i = 1
        for stat in stats:
            print(str(i) + ") " + stat.getName())
        stat = int(input("Please choose and option: ")) - 1
        stats[stat].runStat(dashes)
    elif choice == 5:
        exit(0)
    else:
        print("That is not a valid choice")
