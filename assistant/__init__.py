from assistant.Export import exportToFile
from assistant.Import import importJSON, importManual
from assistant.StatLoader import findStats, loadStat

dashes = importJSON("dashes.json")
stats = findStats()

while True:
    print("What would you like to do?")
    print("1) add dash")
    print("2) print dashes")
    print("3) export")
    print("4) run statistic")
    print("5) exit")
    inStr = input("Please choose an option: ")
    choice = 0
    try:
        choice = int(inStr)
    except:
        print("Invalid input. Please enter a valid number")
        continue

    if choice == 1:
        dashes.addDash(importManual())
        exportToFile(dashes, "dashes.json")
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
            print(str(i) + ") " + stat["name"])
            i += 1

        stat = 0
        while True:
            statStr = input("Please choose and option: ")
            try:
                stat = int(statStr)
                break
            except:
                print("Invalid input. Please enter a valid number")

        tempStat = loadStat(stats[stat])
        print()
        tempStat.runStat(dashes)
    elif choice == 5:
        exit(0)
    else:
        print("That is not a valid choice")
