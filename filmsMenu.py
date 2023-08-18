import addFilms, updateFilms, deleteFilms, filmsReports
from readFilms import read

def filmsMenuOptions():
    options = 0

    optionsList = ["1", "2", "3", "4", "5", "6"]

    userChoices = "Films MenuOptions\nEnter:\n1. Print.\n2. Add.\n3. Update.\n4. Delete.\n5. Reports.\n6. Exit."
    while options not in optionsList: 
        print(userChoices)

        options = input("Enter an option from the Films menu choices above: ")

        if options not in optionsList:
            print(f"(options) is not a valid choice in the Films menu")
    return options

def reportOptions():        
    options = 0             
    optionsList = ["1", "2", "3", "4"]       
    userChoices = "Films reportOptions\nEnter:\n1. All Records Report.\n2. Particular Year Report.\n3. Particular Genre Report.\n4. Particular Rating Report."
    while options not in optionsList:           
        print(userChoices)
        options = input("Enter an report option: ")     
        if options not in optionsList:          
            print(f"(options) invalid choice")
    return options      


mainProgram = True
print(type(mainProgram))
while mainProgram:  
    mainMenu = filmsMenuOptions()

    if mainMenu == "1":
        read()
    elif mainMenu == "2":
        addFilms.insert()
    elif mainMenu == "3":
        updateFilms.update()
    elif mainMenu == "4":
        deleteFilms.delete()
    elif mainMenu == "5":
        reportProgram = True       
        while reportProgram:  
            reportMenu = reportOptions() 
            if reportMenu == "1":
                print("This is report")
                filmsReports.reportsAll()
            elif reportMenu == "2":
                filmsReports.tableReport()
            elif reportMenu == "3":
                filmsReports.tableReport2()
            elif reportMenu == "4":
                filmsReports.tableReport3()
            else:
                reportProgram = False
                input("Press enter to exit report program")
    else:
        mainProgram = False
        input("Press enter to exit the program")