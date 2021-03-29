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
        choice = int(input("Enter your choice [1-%d]: " % len(ageGroup_options)))

        if choice>=1 and choice <= 8:
            cursor.execute("SELECT COUNT(*) FROM BackgroundInfo WHERE ageGroup=%s", (choice,)) 
            print("There were", cursor.fetchone()[0], "confirmed cases of COVID-19 that was in this age group:", ageGroup_options[choice-1])
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
    while True:
        print (30 * "-" , "MENU" , 30 * "-")

        print("Region")
        for i, option in enumerate(region_options_all):
            print("\t%s)" % (i+1), option)
        regionChoice = input("Input as a list separated by commas and press enter: ")

        print("Timeline")
        for i, option in enumerate(timeline_options_all):
            print("\t%s)" % (i+1), option)
        timeLineChoice = input("Input as a list separated by commas and press enter: ")

        print("Gender")
        for i, option in enumerate(gender_options_all):
            print("\t%s)" % (i+1), option)
        genderChoice = input("Input as a list separated by commas and press enter: ")

        print("Age Group")
        for i, option in enumerate(ageGroup_options_all):
            print("\t%s)" % (i+1), option)
        ageGroupChoice = input("Input as a list separated by commas and press enter: ")

        print("Occupation")
        for i, option in enumerate(occupation_options_all):
            print("\t%s)" % (i+1), option)
        occupationChoice = input("Input as a list separated by commas and press enter: ")

        print (67 * "-")

        # SQL Generation
        regionList = regionChoice.split(",")
        timeLineList = timeLineChoice.split(",")
        genderList = genderChoice.split(",")
        ageGroupList = ageGroupChoice.split(",")
        occupationList = occupationChoice.split(",")

        choice = input("Would you like to continue [y/n]: ")

        if choice == 'N' or choice == 'n' or choice == 'No' or choice == 'no':
            break
        elif choice == 'Y' or choice == 'y' or choice == 'Yes' or choice == 'yes':
            continue
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return