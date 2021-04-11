from menu import *
from mysqlInformation import *

def region_loop_transmissions(a, t):

    newRegionOptionsFromDb = getNewRegionOptions()   

    while True:
        region_menu()
        try:
            choice = int(input("Enter your choice [1-%d]: " % len(newRegionOptionsFromDb)))

            if choice >= 1 and choice <= (len(newRegionOptionsFromDb)-1):
                if (a != 3 and t == 3):
                    cursor.execute("select count(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.region=%s and asymptomatic=%s and tranmissions=%s", (choice, a, 9,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 in the", newRegionOptionsFromDb[choice-1], "region." )
                elif (t != 3 and a == 3):
                    cursor.execute("select count(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.region=%s and asymptomatic=%s and tranmissions=%s", (choice, 9, t,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 in the", newRegionOptionsFromDb[choice-1], "region." )
                elif (a != 3 and t != 3):
                    cursor.execute("select count(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.region=%s and asymptomatic=%s and tranmissions=%s", (choice, a, t,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 in the", newRegionOptionsFromDb[choice-1], "region." )
                elif (a == 3 and t == 3):
                    cursor.execute("select count(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.region=%s and asymptomatic=%s and tranmissions=%s", (choice, 9, 9,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 in the", newRegionOptionsFromDb[choice-1], "region." )
                else:
                    cursor.execute("select count(*) from Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID where BackgroundInfo.region=%s", (choice,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 in the", newRegionOptionsFromDb[choice-1], "region." )
            elif choice==len(newRegionOptionsFromDb):
                break
            else:
                input("Wrong option selection. Enter any key to try again..")

        except ValueError:
            cursor.execute("SELECT COUNT(*) FROM Transmissions") 
            print("There were", cursor.fetchone()[0], "total transmissions from COVID-19.")
    return 

def timeline_loop_transmissions(a, t):
    while True:
        timeline_menu()
        try:
            choice = int(input("Enter your choice [1-%d]: " % len(timeline_options)))

            if choice>=1 and choice <= 8:
                if (a != 3 and t == 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.episodeWeek=%s and asymptomatic=%s and tranmissions=%s", (choice+35, a, 9,)) 
                    print("For", timeline_options[choice-1], "there were", cursor.fetchone()[0], "transmissions due to COVID-19.")
                elif (t != 3 and a == 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.episodeWeek=%s and asymptomatic=%s and tranmissions=%s", (choice+35, 9, t,)) 
                    print("For", timeline_options[choice-1], "there were", cursor.fetchone()[0], "transmissions due to COVID-19.")
                elif (a != 3 and t != 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.episodeWeek=%s and asymptomatic=%s and tranmissions=%s", (choice+35, a, t,)) 
                    print("For", timeline_options[choice-1], "there were", cursor.fetchone()[0], "transmissions due to COVID-19.")
                elif (a == 3 and t == 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.episodeWeek=%s and asymptomatic=%s and tranmissions=%s", (choice+35, 9, 9,)) 
                    print("For", timeline_options[choice-1], "there were", cursor.fetchone()[0], "transmissions due to COVID-19.")
                else:
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.episodeWeek=%s", (choice+35,)) 
                    print("For", timeline_options[choice-1], "there were", cursor.fetchone()[0], "transmissions due to COVID-19.")
            elif choice==9:
                break
            else:
                input("Wrong option selection. Enter any key to try again..")
        except ValueError:
            cursor.execute("SELECT COUNT(*) FROM Transmissions") 
            print("There were", cursor.fetchone()[0], "total transmissions from COVID-19.")
 
    return 

def gender_loop_transmissions(a, t):
    while True:
        gender_menu()

        try:
            choice = int(input("Enter your choice [1-%d]: " % len(gender_options)))

            if choice>=1 and choice <= 2:
                if (a != 3 and t == 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.gender=%s and asymptomatic=%s and tranmissions=%s", (choice, a, 9,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 whose gender was", gender_options[choice-1])
                elif (t != 3 and a == 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.gender=%s and asymptomatic=%s and tranmissions=%s", (choice, 9, t,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 whose gender was", gender_options[choice-1])
                elif (a != 3 and t != 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.gender=%s and asymptomatic=%s and tranmissions=%s", (choice, a, t,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 whose gender was", gender_options[choice-1])
                elif (a == 3 and t == 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.gender=%s and asymptomatic=%s and tranmissions=%s", (choice, 9, 9,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 whose gender was", gender_options[choice-1])
                else:
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.gender=%s", (choice,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 whose gender was", gender_options[choice-1])
            elif choice==3:
                if (a != 3 and t == 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.gender=%s and asymptomatic=%s and tranmissions=%s", (9, a, 9,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 whose gender was", gender_options[choice-1])
                elif (t != 3 and a == 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.gender=%s and asymptomatic=%s and tranmissions=%s", (9, 9, t,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 whose gender was", gender_options[choice-1])
                elif (a != 3 and t != 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.gender=%s and asymptomatic=%s and tranmissions=%s", (9, a, t,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 whose gender was", gender_options[choice-1])
                elif (a == 3 and t == 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.gender=%s and asymptomatic=%s and tranmissions=%s", (9, 9, 9,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 whose gender was", gender_options[choice-1])
                else:
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.gender=%s", (9,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 whose gender was", gender_options[choice-1])
            elif choice==4:
                break
            else:
                input("Wrong option selection. Enter any key to try again..")
        except ValueError:
            cursor.execute("SELECT COUNT(*) FROM Transmissions") 
            print("There were", cursor.fetchone()[0], "total transmissions from COVID-19.")
    return

def agegroup_loop_transmissions(a, t):
    while True:
        ageGroup_menu()

        try:
            choice = int(input("Enter your choice [1-%d]: " % len(ageGroup_options)))

            if choice>=1 and choice <= 8:
                if (a != 3 and t == 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.ageGroup=%s and asymptomatic=%s and tranmissions=%s", (choice, a, 9,)) 
                    print("There were", cursor.fetchone()[0], "confirmed death due to COVID-19 that was in this age group:", ageGroup_options[choice-1])
                elif (t != 3 and a == 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.ageGroup=%s and asymptomatic=%s and tranmissions=%s", (choice, 9, t,)) 
                    print("There were", cursor.fetchone()[0], "confirmed death due to COVID-19 that was in this age group:", ageGroup_options[choice-1])
                elif (a != 3 and t != 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.ageGroup=%s and asymptomatic=%s and tranmissions=%s", (choice, a, t,)) 
                    print("There were", cursor.fetchone()[0], "confirmed death due to COVID-19 that was in this age group:", ageGroup_options[choice-1])
                elif (a == 3 and t == 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.ageGroup=%s and asymptomatic=%s and tranmissions=%s", (choice, 9, 9,)) 
                    print("There were", cursor.fetchone()[0], "confirmed death due to COVID-19 that was in this age group:", ageGroup_options[choice-1])
                else:
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.ageGroup=%s", (choice,)) 
                    print("There were", cursor.fetchone()[0], "confirmed death due to COVID-19 that was in this age group:", ageGroup_options[choice-1])
            elif choice==9:
                break
            else:
                input("Wrong option selection. Enter any key to try again..")
        except ValueError:
            cursor.execute("SELECT COUNT(*) FROM Transmissions") 
            print("There were", cursor.fetchone()[0], "total transmissions from COVID-19.")
    
    return

def occupation_loop_transmissions(a, t):
    while True:
        occupation_menu()

        try:
            choice = int(input("Enter your choice [1-%d]: " % len(occupation_options)))

            if choice>=1 and choice<=4:
                if (a != 3 and t == 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.occupation=%s and asymptomatic=%s and tranmissions=%s", (choice, a, 9,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 whose occupation was", occupation_options[choice-1])
                elif (t != 3 and a == 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.occupation=%s and asymptomatic=%s and tranmissions=%s", (choice, 9, t,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 whose occupation was", occupation_options[choice-1])
                elif (a != 3 and t != 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.occupation=%s and asymptomatic=%s and tranmissions=%s", (choice, a, t,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 whose occupation was", occupation_options[choice-1])
                elif (a == 3 and t == 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.occupation=%s and asymptomatic=%s and tranmissions=%s", (choice, 9, 9,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 whose occupation was", occupation_options[choice-1])
                else:
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.occupation=%s", (choice,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 whose occupation was", occupation_options[choice-1])
            elif choice==5:
                if (a != 3 and t == 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.occupation=%s and asymptomatic=%s and tranmissions=%s", (9, a, 9,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 whose occupation was", occupation_options[choice-1])
                elif (t != 3 and a == 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.occupation=%s and asymptomatic=%s and tranmissions=%s", (9, 9, t,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 whose occupation was", occupation_options[choice-1])
                elif (a != 3 and t != 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.occupation=%s and asymptomatic=%s and tranmissions=%s", (9, a, t,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 whose occupation was", occupation_options[choice-1])
                elif (a == 3 and t == 3):
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.occupation=%s and asymptomatic=%s and tranmissions=%s", (9, 9, 9,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 whose occupation was", occupation_options[choice-1])
                else: 
                    cursor.execute("SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE BackgroundInfo.occupation=%s", (9,)) 
                    print("There were", cursor.fetchone()[0], "transmissions due to COVID-19 whose occupation was", occupation_options[choice-1])
            elif choice==6:
                break
            else:
                input("Wrong option selection. Enter any key to try again..")
        except ValueError:
            cursor.execute("SELECT COUNT(*) FROM Transmissions") 
            print("There were", cursor.fetchone()[0], "total transmissions from COVID-19.")
    
    return

def allTransmissions():
    cursor.execute("SELECT COUNT(*) FROM Transmissions") 
    print("There were a total of ", cursor.fetchone()[0], "transmissions due to COVID-19")
    
def combinedFilter_loop_transmissions(a, t):
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

        if str(len(newRegionOptionsFromDb)) in regionChoice and \
            str(len(timeline_options_all)) in timeLineChoice and \
            str(len(gender_options_all)) in genderChoice and \
            str(len(ageGroup_options_all)) in ageGroupChoice and \
            str(len(occupation_options_all)) in occupationChoice and \
            str(len(hospitalization_options_all)) in hospitilizationChoice:
            baseQuery = "SELECT COUNT(*) FROM Transmissions WHERE" 
            if (a != 3):
                baseQuery += "asymptomatic=%s AND " % a 
            elif (a == 3):
                baseQuery += "asymptomatic=%s AND " % 9 
            
            if (t != 3):
                baseQuery += "tranmissions=%s" % t 
            elif (t == 3):
                baseQuery += "tranmissions=%s" % 9 
        else:
            baseQuery = "SELECT COUNT(*) FROM Transmissions inner join BackgroundInfo on Transmissions.caseID = BackgroundInfo.caseID WHERE "

            if (a != 3):
                baseQuery += "asymptomatic=%s AND " % a 
            elif (a == 3):
                baseQuery += "asymptomatic=%s AND " % 9 
            
            if (t != 3):
                baseQuery += "tranmissions=%s AND " % t 
            elif (t == 3):
                baseQuery += "tranmissions=%s AND " % 9

            if regionChoice and (str(len(newRegionOptionsFromDb)) not in regionChoice):
                baseQuery += "BackgroundInfo.region IN (%s) AND " % regionChoice

            if timeLineChoice and (str(len(timeline_options_all)) not in timeLineChoice):
                newTimeLineChoice = timeLineChoice.split(",")
                for i in range (len(newTimeLineChoice)):
                    newTimeLineChoice[i] = str(int(newTimeLineChoice[i])+35)
                timeLineChoice = ','.join(newTimeLineChoice)
                baseQuery += "BackgroundInfo.episodeWeek IN (%s) AND " % timeLineChoice

            if genderChoice and (str(len(gender_options_all)) not in genderChoice):
                baseQuery += "BackgroundInfo.gender IN (%s) AND " % genderChoice

            if ageGroupChoice and (str(len(ageGroup_options_all)) not in ageGroupChoice):
                baseQuery += "BackgroundInfo.ageGroup IN (%s) AND " % ageGroupChoice

            if occupationChoice and (str(len(occupation_options_all)) not in occupationChoice):
                baseQuery += "BackgroundInfo.occupation IN (%s)" % occupationChoice

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
