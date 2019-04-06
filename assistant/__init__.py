import readline

from assistant.Completer import Completer
from assistant.Export import exportToFile
from assistant.Import import importJSON, importManual
from assistant.StatLoader import findStats, loadStat

dashes = importJSON("dashes.json")
stats = findStats()

optionComp = Completer(['add', 'print', 'export', 'stat', 'exit', 'help'])

readline.parse_and_bind("tab: complete")
readline.set_completer_delims('')

while True:
    readline.set_completer(optionComp.complete)
    choice = input(">")
    readline.set_completer(None)

    if choice == "add":
        dashes.addDash(importManual(dashes.restaurants, dashes.regions))
        exportToFile(dashes, "dashes.json")
    elif choice == "print":
        i = 1
        for dash in dashes.dashes:
            print("Dash " + str(i))
            dash.print()
            print()
            i += 1
    elif choice == "export":
        print("Exporting...")
        exportToFile(dashes, "dashes.json")
    elif choice == "stat":
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
                if stat > 0 and stat < i:
                    break
                else:
                    print("Invalid option. Please choose one of the options displayed")
            except:
                print("Invalid input. Please enter a valid number")


        tempStat = loadStat(stats[stat - 1])
        print()
        tempStat.runStat(dashes)
    elif choice == "help":
        print("Options for commands:")
        print("  add- add dash")
        print("  print- print all dashes")
        print("  export- export dashes to json file")
        print("  stat- run a statistic")
        print("  help- display this help info")
        print("  exit- exit the program")
    elif choice == "exit":
        exit(0)
    else:
        print("That is not a valid command. If you need help, type help.")
