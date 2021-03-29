from menu import *
from mysqlInformation import *

def region_testing_loop():
    while True:
        region_menu()
        choice = int(input("Enter your choice [1-6]: "))

        if choice >= 1 and choice <=5:
            cursor.execute("select sum(DailyTested) from WeeklyTesting where WeeklyTesting.region=%s", (choice,)) 
            print("There were", cursor.fetchone()[0], "COVID-19 tests conducted in the", region_options[choice-1], "region." )
        elif choice==6:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    return 

def timeline_testing_loop():
    while True:
        timeline_menu()
        choice = int(input("Enter your choice [1-9]: "))

        if choice>=1 and choice <= 8:
            cursor.execute("SELECT sum(DailyTested) FROM WeeklyTesting WHERE WeeklyTesting.episodeWeek=%s", (choice+35,)) 
            print("For", timeline_options[choice-1], "there were", cursor.fetchone()[0], "confirmed COVID-19 conducted.")
        elif choice==9:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return

def regionAndTimeline_loop():
    print("Region and Timeline")