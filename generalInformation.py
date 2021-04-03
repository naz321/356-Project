from menu import *
from mysqlInformation import *

def region_loop():
    while True:
        region_menu()

        try:
            choice = int(input("Enter your choice [1-%d]: " % len(region_options)))

            if choice >= 1 and choice <=5:
                cursor.execute("SELECT COUNT(*) FROM BackgroundInfo WHERE region=%s", (choice,)) 
                print("There were", cursor.fetchone()[0], "confirmed cases of COVID-19 in the", region_options[choice-1], "region." )
            elif choice==6:
                break
            else:
                input("Wrong option selection. Enter any key to try again..")
        except ValueError:
            cursor.execute("SELECT COUNT(*) FROM BackgroundInfo") 
            print("There were", cursor.fetchone()[0], "total confirmed cases of COVID-19." )
    
    return 

def timeline_loop():
    while True:
        timeline_menu()

        try: 
            choice = int(input("Enter your choice [1-%d]: " % len(timeline_options)))

            if choice>=1 and choice <= 8:
                cursor.execute("SELECT COUNT(*) FROM BackgroundInfo WHERE episodeWeek=%s", (choice+35,)) 
                print("For", timeline_options[choice-1], "there were", cursor.fetchone()[0], "confirmed cases of COVID-19.")
            elif choice==9:
                break
            else:
                input("Wrong option selection. Enter any key to try again..")
        except ValueError:
            cursor.execute("SELECT COUNT(*) FROM BackgroundInfo") 
            print("There were", cursor.fetchone()[0], "total confirmed cases of COVID-19." )
    
    return 

def gender_loop():
    while True:
        gender_menu()

        try:
            choice = int(input("Enter your choice [1-%d]: " % len(gender_options)))

            if choice>=1 and choice <= 2:
                cursor.execute("SELECT COUNT(*) FROM BackgroundInfo WHERE gender=%s", (choice,)) 
                print("There were", cursor.fetchone()[0], "confirmed cases of COVID-19 whose gender was", gender_options[choice-1])
            elif choice==3:
                cursor.execute("SELECT COUNT(*) FROM BackgroundInfo WHERE gender=%s", (9,)) 
                print("There were", cursor.fetchone()[0], "confirmed cases of COVID-19 whose gender was", gender_options[choice-1])
            elif choice==4:
                break
            else:
                input("Wrong option selection. Enter any key to try again..")
        except ValueError:
            cursor.execute("SELECT COUNT(*) FROM BackgroundInfo") 
            print("There were", cursor.fetchone()[0], "total confirmed cases of COVID-19." )
    
    return

def agegroup_loop():
    while True:
        ageGroup_menu()

        try:
            choice = int(input("Enter your choice [1-%d]: " % len(ageGroup_options)))

            if choice>=1 and choice <= 8:
                cursor.execute("SELECT COUNT(*) FROM BackgroundInfo WHERE ageGroup=%s", (choice,)) 
                print("There were", cursor.fetchone()[0], "confirmed cases of COVID-19 that was in this age group:", ageGroup_options[choice-1])
            elif choice==9:
                break
            else:
                input("Wrong option selection. Enter any key to try again..")
        except ValueError:
            cursor.execute("SELECT COUNT(*) FROM BackgroundInfo") 
            print("There were", cursor.fetchone()[0], "total confirmed cases of COVID-19." )
    
    return

def occupation_loop():
    while True:
        occupation_menu()

        try:
            choice = int(input("Enter your choice [1-%d]: " % len(occupation_options)))

            if choice>=1 and choice<=4:
                cursor.execute("SELECT COUNT(*) FROM BackgroundInfo WHERE occupation=%s", (choice,)) 
                print("There were", cursor.fetchone()[0], "confirmed cases of COVID-19 whose occupation was", occupation_options[choice-1])
            elif choice==5:
                cursor.execute("SELECT COUNT(*) FROM BackgroundInfo WHERE occupation=%s", (9,)) 
                print("There were", cursor.fetchone()[0], "confirmed cases of COVID-19 whose occupation was", occupation_options[choice-1])
            elif choice==6:
                break
            else:
                input("Wrong option selection. Enter any key to try again..")
        except ValueError:
            cursor.execute("SELECT COUNT(*) FROM BackgroundInfo") 
            print("There were", cursor.fetchone()[0], "total confirmed cases of COVID-19." )
    
    return

def combinedFilter_loop():
    while True:
        print (30 * "-" , "MENU" , 30 * "-")

        print("Region")
        while True:
            for i, option in enumerate(region_options_all):
                print("\t%s)" % (i+1), option)
            regionChoice = input("Input as a list separated by commas and press enter: ") or str(len(region_options_all))

            invalidChoice = 0
            for choice in regionChoice.split(","):
                if int(choice) > len(region_options_all):
                    input("Wrong option selection. Enter any key to try again..")
                    invalidChoice = -1
                    break

            if invalidChoice == -1:
                continue
            else:
                break

        print("Timeline")
        while True:
            for i, option in enumerate(timeline_options_all):
                print("\t%s)" % (i+1), option)
            timeLineChoice = input("Input as a list separated by commas and press enter: ") or str(len(timeline_options_all))

            invalidChoice = 0
            for choice in timeLineChoice.split(","):
                if int(choice) > len(timeline_options_all):
                    input("Wrong option selection. Enter any key to try again..")
                    invalidChoice = -1
                    break

            if invalidChoice == -1:
                continue
            else:
                break

        print("Gender")
        while True:
            for i, option in enumerate(gender_options_all):
                print("\t%s)" % (i+1), option)
            genderChoice = input("Input as a list separated by commas and press enter: ") or str(len(gender_options_all))

            invalidChoice = 0
            for choice in genderChoice.split(","):
                if int(choice) > len(gender_options_all):
                    input("Wrong option selection. Enter any key to try again..")
                    invalidChoice = -1
                    break

            if invalidChoice == -1:
                continue
            else:
                break

        print("Age Group")
        while True:
            for i, option in enumerate(ageGroup_options_all):
                print("\t%s)" % (i+1), option)
            ageGroupChoice = input("Input as a list separated by commas and press enter: ") or str(len(ageGroup_options_all))

            invalidChoice = 0
            for choice in ageGroupChoice.split(","):
                if int(choice) > len(ageGroup_options_all):
                    input("Wrong option selection. Enter any key to try again..")
                    invalidChoice = -1
                    break

            if invalidChoice == -1:
                continue
            else:
                break

        print("Occupation")
        while True:
            for i, option in enumerate(occupation_options_all):
                print("\t%s)" % (i+1), option)
            occupationChoice = input("Input as a list separated by commas and press enter: ") or str(len(occupation_options_all))

            invalidChoice = 0
            for choice in occupationChoice.split(","):
                if int(choice) > len(occupation_options_all):
                    input("Wrong option selection. Enter any key to try again..")
                    invalidChoice = -1
                    break

            if invalidChoice == -1:
                continue
            else:
                break

        print (67 * "-")

        if str(len(region_options_all)) in regionChoice and \
            str(len(timeline_options_all)) in timeLineChoice and \
            str(len(gender_options_all)) in genderChoice and \
            str(len(ageGroup_options_all)) in ageGroupChoice and \
            str(len(occupation_options_all)) in occupationChoice:
            baseQuery = "SELECT COUNT(*) FROM BackgroundInfo"
        else:
            baseQuery = "SELECT COUNT(*) FROM BackgroundInfo WHERE "

            if regionChoice and (str(len(region_options_all)) not in regionChoice):
                baseQuery += "region IN (%s) AND " % regionChoice

            if timeLineChoice and (str(len(timeline_options_all)) not in timeLineChoice):
                newTimeLineChoice = timeLineChoice.split(",")
                for i in range (len(newTimeLineChoice)):
                    newTimeLineChoice[i] = str(int(newTimeLineChoice[i])+35)
                timeLineChoice = ','.join(newTimeLineChoice)
                baseQuery += "episodeWeek IN (%s) AND " % timeLineChoice

            if genderChoice and (str(len(gender_options_all)) not in genderChoice):
                baseQuery += "gender IN (%s) AND " % genderChoice

            if ageGroupChoice and (str(len(ageGroup_options_all)) not in ageGroupChoice):
                baseQuery += "ageGroup IN (%s) AND " % ageGroupChoice

            if occupationChoice and (str(len(occupation_options_all)) not in occupationChoice):
                baseQuery += "occupation IN (%s)" % occupationChoice

        # Remove any unncessary "AND"
        # example: SELECT COUNT(*) FROM BackgroundInfo WHERE region IN (1) AND
        if "AND" in baseQuery[-4:]:
            baseQuery = baseQuery[:-4]
        
        # print(baseQuery)
        cursor.execute(baseQuery) 
        print("Based on your query there were", cursor.fetchone()[0], "confirmed cases of COVID-19.")
 
        choice = input("Would you like to continue [y/n]: ")

        if choice == 'N' or choice == 'n' or choice == 'No' or choice == 'no':
            break
        elif choice == 'Y' or choice == 'y' or choice == 'Yes' or choice == 'yes':
            continue
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return