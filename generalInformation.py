from menu import *
from mysqlInformation import *

def region_loop():
    while True:
        region_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(region_options)))

        if choice >= 1 and choice <=5:
            cursor.execute("SELECT COUNT(*) FROM BackgroundInfo WHERE region=%s", (choice,)) 
            print("There were", cursor.fetchone()[0], "confirmed cases of COVID-19 in the", region_options[choice-1], "region." )
        elif choice==6:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return 

def timeline_loop():
    while True:
        timeline_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(timeline_options)))

        if choice>=1 and choice <= 8:
            cursor.execute("SELECT COUNT(*) FROM BackgroundInfo WHERE episodeWeek=%s", (choice+35,)) 
            print("For", timeline_options[choice-1], "there were", cursor.fetchone()[0], "confirmed cases of COVID-19.")
        elif choice==9:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return 

def gender_loop():
    while True:
        gender_menu()
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
    
    return

def agegroup_loop():
    while True:
        ageGroup_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(ageGroup_Options)))

        if choice>=1 and choice <= 8:
            cursor.execute("SELECT COUNT(*) FROM BackgroundInfo WHERE ageGroup=%s", (choice,)) 
            print("There were", cursor.fetchone()[0], "confirmed cases of COVID-19 that was in this age group:", ageGroup_Options[choice-1])
        elif choice==9:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return

def occupation_loop():
    while True:
        occupation_menu()
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
    
    return

def combinedFilter_loop():
    print("Combined Filter")