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
    print("Region and Timeline")