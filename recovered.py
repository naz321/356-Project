from menu import *
from mysqlInformation import *

def region_loop_recovered():
    while True:
        region_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(region_options)))

        if choice >= 1 and choice <=5:
            cursor.execute("select count(*) FROM Recovered inner join BackgroundInfo on Recovered.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.region=%s", (choice,)) 
            print("There were", cursor.fetchone()[0], "recovered cases of COVID-19 in the", region_options[choice-1], "region." )
        elif choice==6:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return 

def timeline_loop_recovered():
    while True:
        timeline_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(timeline_options)))

        if choice>=1 and choice <= 8:
            cursor.execute("SELECT COUNT(*) FROM Recovered inner join BackgroundInfo on Recovered.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.episodeWeek=%s", (choice+35,)) 
            print("For", timeline_options[choice-1], "there were", cursor.fetchone()[0], "recovered cases of COVID-19.")
        elif choice==9:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return 

def gender_loop_recovered():
    while True:
        gender_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(gender_options)))

        if choice>=1 and choice <= 2:
            cursor.execute("SELECT COUNT(*) FROM Recovered inner join BackgroundInfo on Recovered.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.gender=%s", (choice,)) 
            print("There were", cursor.fetchone()[0], "recovered cases of COVID-19 whose gender was", gender_options[choice-1])
        elif choice==3:
            cursor.execute("SELECT COUNT(*) FROM Recovered inner join BackgroundInfo on Recovered.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.gender=%s", (9,)) 
            print("There were", cursor.fetchone()[0], "recovered cases of COVID-19 whose gender was", gender_options[choice-1])
        elif choice==4:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return

def agegroup_loop_recovered():
    while True:
        ageGroup_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(ageGroup_Options)))

        if choice>=1 and choice <= 8:
            cursor.execute("SELECT COUNT(*) FROM Recovered inner join BackgroundInfo on Recovered.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.ageGroup=%s", (choice,)) 
            print("There were", cursor.fetchone()[0], "recovered cases of COVID-19 that was in this age group:", ageGroup_Options[choice-1])
        elif choice==9:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return

def occupation_loop_recovered():
    while True:
        occupation_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(occupation_options)))

        if choice>=1 and choice<=4:
            cursor.execute("SELECT COUNT(*) FROM Recovered inner join BackgroundInfo on Recovered.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.occupation=%s", (choice,)) 
            print("There were", cursor.fetchone()[0], "recovered cases of COVID-19 whose occupation was", occupation_options[choice-1])
        elif choice==5:
            cursor.execute("SELECT COUNT(*) FROM Recovered inner join BackgroundInfo on Recovered.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.occupation=%s", (9,)) 
            print("There were", cursor.fetchone()[0], "recovered cases of COVID-19 whose occupation was", occupation_options[choice-1])
        elif choice==6:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")

    return

def hospitalization_loop_recovered():
    while True:
        hospitalization_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(hospitalization_options)))

        if choice>=1 and choice<=3:
            cursor.execute("SELECT COUNT(*) FROM Recovered WHERE hospitalStatus=%s", (choice,)) 
            print("There were", cursor.fetchone()[0], "recovered cases of COVID-19 whose hospital status was", hospitalization_options[choice-1])
        elif choice==4:
            cursor.execute("SELECT COUNT(*) FROM Recovered WHERE hospitalStatus=%s", (9,)) 
            print("There were", cursor.fetchone()[0], "recovered cases of COVID-19 whose hospital status was", hospitalization_options[choice-1])
        elif choice==5:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return

def allRecovered():
    cursor.execute("SELECT COUNT(*) FROM Recovered") 
    print("There were a total of ", cursor.fetchone()[0], "recovered cases of COVID-19 ")
    
def combinedFilter_loop_recovered():
    print("Combined Filter")