from menu import *
from mysqlInformation import *

def region_testing_loop():
    newRegionOptionsFromDb = getNewRegionOptions()   

    while True:
        region_menu()

        try: 
            choice = int(input("Enter your choice [1-%d]: " % len(newRegionOptionsFromDb)))
            if choice >= 1 and choice <= (len(newRegionOptionsFromDb)-1):
                cursor.execute("select sum(DailyTested) from WeeklyTesting where WeeklyTesting.region=%s", (choice,)) 
                numTesting = cursor.fetchone()[0]
                if numTesting == None:
                    numTesting = 0
                print("There were", numTesting, "COVID-19 tests conducted in the", newRegionOptionsFromDb[choice-1], "region." )
            elif choice==len(newRegionOptionsFromDb):
                break
            else:
                input("Wrong option selection. Enter any key to try again..")
        except ValueError:
            cursor.execute("select sum(DailyTested) from WeeklyTesting") 
            print("There were", cursor.fetchone()[0], "total testing done.")

    return

def timeline_testing_loop():
    while True:
        timeline_menu()

        try: 
            choice = int(input("Enter your choice [1-9]: "))
            if choice>=1 and choice <= 8:
                cursor.execute("SELECT sum(DailyTested) FROM WeeklyTesting WHERE WeeklyTesting.episodeWeek=%s", (choice+35,)) 
                print("For", timeline_options[choice-1], "there were", cursor.fetchone()[0], "confirmed COVID-19 conducted.")
            elif choice==9:
                break
            else:
                input("Wrong option selection. Enter any key to try again..")
        except ValueError:
            cursor.execute("select sum(DailyTested) from WeeklyTesting") 
            print("There were", cursor.fetchone()[0], "total testing done.")
    
    return

def regionAndTimeline_loop():
    while True:
        print (30 * "-" , "MENU" , 30 * "-")

        print("Region")
        newRegionOptionsFromDb = getNewRegionOptions()
        newRegionOptionsFromDb[-1] = "All"  
        while True:
            for i, option in enumerate(newRegionOptionsFromDb):
                print("\t%s)" % (i+1), option)
            regionChoice = input("Input as a list separated by commas and press enter: ") or str(len(newRegionOptionsFromDb))

            invalidChoice = 0
            for choice in regionChoice.split(","):
                if int(choice) > len(newRegionOptionsFromDb):
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
        
        print (67 * "-")

        if str(len(newRegionOptionsFromDb)) in regionChoice and \
            str(len(timeline_options_all)) in timeLineChoice:
            baseQuery = "SELECT COUNT(*) FROM WeeklyTesting"
        else:
            baseQuery = "SELECT COUNT(*) FROM WeeklyTesting WHERE "

            if regionChoice and (str(len(newRegionOptionsFromDb)) not in regionChoice):
                baseQuery += " region IN (%s) AND " % regionChoice

            if timeLineChoice and (str(len(timeline_options_all)) not in timeLineChoice):
                newTimeLineChoice = timeLineChoice.split(",")
                for i in range (len(newTimeLineChoice)):
                    newTimeLineChoice[i] = str(int(newTimeLineChoice[i])+35)
                timeLineChoice = ','.join(newTimeLineChoice)
                baseQuery += "episodeWeek IN (%s) AND " % timeLineChoice

        # Remove any unncessary "AND"
        # example: SELECT COUNT(*) FROM BackgroundInfo WHERE region IN (1) AND
        if "AND" in baseQuery[-4:]:
            baseQuery = baseQuery[:-4]
        
        # print(baseQuery)
        cursor.execute(baseQuery) 
        print("Based on your query there were", cursor.fetchone()[0], "transmissions due to COVID-19.")
 
        choice = input("Would you like to continue [y/n]: ")

        if choice == 'N' or choice == 'n' or choice == 'No' or choice == 'no':
            break
        elif choice == 'Y' or choice == 'y' or choice == 'Yes' or choice == 'yes':
            continue
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return
