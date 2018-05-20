from assistant.Export import exportToFile
from assistant.Import import importJSON, importManual

dashes = importJSON("dashes.json")

while True:
    print("What would you like to do?")
    print("1) add dash")
    print("2) print dashes")
    print("3) export")
    print("4) exit")
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
        exit(0)
    else:
        print("That is not a valid choice")
