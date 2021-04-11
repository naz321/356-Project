from menu import *
from mysqlInformation import *

def region_loop_transmissions(a, t):
    while True:
        region_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(region_options)))

        if choice >= 1 and choice <=5:
            if (a != 3 and t == 3):
                cursor.execute("select count(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.region=%s and asymptomatic=%s", (choice, a,)) 
                print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 in the", region_options[choice-1], "region." )
            elif (t != 3 and a == 3):
                cursor.execute("select count(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.region=%s and tranmissions=%s", (choice, t,)) 
                print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 in the", region_options[choice-1], "region." )
            elif (a != 3 and t != 3):
                cursor.execute("select count(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.region=%s and asymptomatic=%s and tranmissions=%s", (choice, a, t,)) 
                print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 in the", region_options[choice-1], "region." )
            else:
                cursor.execute("select count(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.region=%s", (choice,)) 
                print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 in the", region_options[choice-1], "region." )
        elif choice==6:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    return 

def timeline_loop_transmissions(a, t):
    while True:
        timeline_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(timeline_options)))

        if choice>=1 and choice <= 8:
            if (a != 3 and t == 3):
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.episodeWeek=%s and asymptomatic=%s", (choice+35, a,)) 
                print("For", timeline_options[choice-1], "there were", cursor.fetchone()[0], "confirmed deaths due to COVID-19.")
            elif (t != 3 and a == 3):
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.episodeWeek=%s and tranmissions=%s", (choice+35, t,)) 
                print("For", timeline_options[choice-1], "there were", cursor.fetchone()[0], "confirmed deaths due to COVID-19.")
            elif (a != 3 and t != 3):
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.episodeWeek=%s and asymptomatic=%s and tranmissions=%s", (choice+35, a, t,)) 
                print("For", timeline_options[choice-1], "there were", cursor.fetchone()[0], "confirmed deaths due to COVID-19.")
            else:
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.episodeWeek=%s", (choice+35,)) 
                print("For", timeline_options[choice-1], "there were", cursor.fetchone()[0], "confirmed deaths due to COVID-19.")
        elif choice==9:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
 
    return 

def gender_loop_transmissions(a, t):
    while True:
        gender_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(gender_options)))

        if choice>=1 and choice <= 2:
            if (a != 3 and t == 3):
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.gender=%s and asymptomatic=%s", (choice, a,)) 
                print("There were", cursor.fetchone()[0], "confirmed deaths due to COVID-19 whose gender was", gender_options[choice-1])
            elif (t != 3 and a == 3):
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.gender=%s and tranmissions=%s", (choice, t,)) 
                print("There were", cursor.fetchone()[0], "confirmed deaths due to COVID-19 whose gender was", gender_options[choice-1])
            elif (a != 3 and t != 3):
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.gender=%s and asymptomatic=%s and tranmissions=%s", (choice, a, t,)) 
                print("There were", cursor.fetchone()[0], "confirmed deaths due to COVID-19 whose gender was", gender_options[choice-1])
            else:
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.gender=%s", (choice,)) 
                print("There were", cursor.fetchone()[0], "confirmed deaths due to COVID-19 whose gender was", gender_options[choice-1])
        elif choice==3:
            if (a != 3 and t == 3):
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.gender=%s and asymptomatic=%s", (9, a,)) 
                print("There were", cursor.fetchone()[0], "confirmed deaths due to COVID-19 whose gender was", gender_options[choice-1])
            elif (t != 3 and a == 3):
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.gender=%s and tranmissions=%s", (9, t,)) 
                print("There were", cursor.fetchone()[0], "confirmed deaths due to COVID-19 whose gender was", gender_options[choice-1])
            elif (a != 3 and t != 3):
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.gender=%s and asymptomatic=%s and tranmissions=%s", (9, a, t,)) 
                print("There were", cursor.fetchone()[0], "confirmed deaths due to COVID-19 whose gender was", gender_options[choice-1])
            else:
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.gender=%s", (9,)) 
                print("There were", cursor.fetchone()[0], "confirmed deaths due to COVID-19 whose gender was", gender_options[choice-1])
        elif choice==4:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    return

def agegroup_loop_transmissions(a, t):
    while True:
        ageGroup_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(ageGroup_options)))

        if choice>=1 and choice <= 8:
            if (a != 3 and t == 3):
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.ageGroup=%s and asymptomatic=%s", (choice, a,)) 
                print("There were", cursor.fetchone()[0], "confirmed death due to COVID-19 that was in this age group:", ageGroup_options[choice-1])
            elif (t != 3 and a == 3):
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.ageGroup=%s and tranmissions=%s", (choice, t,)) 
                print("There were", cursor.fetchone()[0], "confirmed death due to COVID-19 that was in this age group:", ageGroup_options[choice-1])
            elif (a != 3 and t != 3):
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.ageGroup=%s and asymptomatic=%s and tranmissions=%s", (choice, a, t,)) 
                print("There were", cursor.fetchone()[0], "confirmed death due to COVID-19 that was in this age group:", ageGroup_options[choice-1])
            else:
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.ageGroup=%s", (choice,)) 
                print("There were", cursor.fetchone()[0], "confirmed death due to COVID-19 that was in this age group:", ageGroup_options[choice-1])
        elif choice==9:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return

def occupation_loop_transmissions(a, t):
    while True:
        occupation_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(occupation_options)))

        if choice>=1 and choice<=4:
            if (a != 3 and t == 3):
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.occupation=%s and asymptomatic=%s", (choice, a,)) 
                print("There were", cursor.fetchone()[0], "confirmed deaths due to COVID-19 whose occupation was", occupation_options[choice-1])
            elif (t != 3 and a == 3):
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.occupation=%s and tranmissions=%s", (choice, t,)) 
                print("There were", cursor.fetchone()[0], "confirmed deaths due to COVID-19 whose occupation was", occupation_options[choice-1])
            elif (a != 3 and t != 3):
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.occupation=%s and asymptomatic=%s and tranmissions=%s", (choice, a, t,)) 
                print("There were", cursor.fetchone()[0], "confirmed deaths due to COVID-19 whose occupation was", occupation_options[choice-1])
            else:
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.occupation=%s", (choice,)) 
                print("There were", cursor.fetchone()[0], "confirmed deaths due to COVID-19 whose occupation was", occupation_options[choice-1])
        elif choice==5:
            if (a != 3 and t == 3):
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.occupation=%s and asymptomatic=%s", (9, a,)) 
                print("There were", cursor.fetchone()[0], "confirmed deaths due to COVID-19 whose occupation was", occupation_options[choice-1])
            elif (t != 3 and a == 3):
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.occupation=%s and tranmissions=%s", (9, t,)) 
                print("There were", cursor.fetchone()[0], "confirmed deaths due to COVID-19 whose occupation was", occupation_options[choice-1])
            elif (a != 3 and t != 3):
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.occupation=%s and asymptomatic=%s and tranmissions=%s", (9, a, t,)) 
                print("There were", cursor.fetchone()[0], "confirmed deaths due to COVID-19 whose occupation was", occupation_options[choice-1])
            else: 
                cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.occupation=%s", (9,)) 
                print("There were", cursor.fetchone()[0], "confirmed deaths due to COVID-19 whose occupation was", occupation_options[choice-1])
        elif choice==6:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return

def allTransmissions():
    cursor.execute("SELECT COUNT(*) FROM Transmissions") 
    print("There were a total of ", cursor.fetchone()[0], "transmissions due to COVID-19")
    
# def combinedFilter_loop_death():
#     print("Combined Filter")