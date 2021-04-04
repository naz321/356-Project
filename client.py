from menu import *
from generalInformation import *
from death import *
from recovered import *
from weeklyTesting import *
from transmissions import *

## Text menu in Python

### Global variables
mainLoop=True

def general_information_loop():

    while True:
        general_information_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(background_information_options)))

        if choice==1:
            region_loop()
        elif choice==2:
            timeline_loop()
        elif choice==3:
            gender_loop()
        elif choice==4:
            agegroup_loop()
        elif choice==5:
            occupation_loop()
        elif choice==6:
            combinedFilter_loop()
        elif choice==7:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return

def death_loop():

    while True:
        death_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(death_options)))

        if choice==1:
            region_loop_death()
        elif choice==2:
            timeline_loop_death()
        elif choice==3:
            gender_loop_death()
        elif choice==4:
            agegroup_loop_death()
        elif choice==5:
            occupation_loop_death()
        elif choice==6:
            hospitalization_loop_death()
        elif choice==7:
            allDeaths()
        elif choice==8:
            combinedFilter_loop_death()
        elif choice==9:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return

def recovered_loop():

    while True:
        recovered_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(recovered_options)))

        if choice==1:
            region_loop_recovered()
        elif choice==2:
            timeline_loop_recovered()
        elif choice==3:
            gender_loop_recovered()
        elif choice==4:
            agegroup_loop_recovered()
        elif choice==5:
            occupation_loop_recovered()
        elif choice==6:
            hospitalization_loop_recovered()
        elif choice==7:
            allRecovered()
        elif choice==8:
            combinedFilter_loop_recovered()
        elif choice==9:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return

def transmissions_loop_asymptomatic():
    while True:
        asymptomatic_menu()
        asymptomatic_choice = int(input("Enter your choice [1-%d]: " % len(asymptomatic_options)))

        if asymptomatic_choice >= 1 and asymptomatic_choice <=3:
            transmissions_loop_transmissions_type(asymptomatic_choice)
        elif asymptomatic_choice == 4:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")

    return

def transmissions_loop_transmissions_type(asymp_choice):
    while True: 
        transmissions_type_menu()
        transmission_type_choice = int(input("Enter your choice [1-%d]: " % len(transmissions_type_options)))

        if transmission_type_choice >= 1 and transmission_type_choice <=3:
            transmission_loop(asymp_choice, transmission_type_choice)
        elif transmission_type_choice == 4:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    return 


def transmission_loop(a_choice, t_choice):

    while True:
        transmissions_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(transmissions_options)))

        if choice==1:
            region_loop_transmissions(a_choice, t_choice)
        elif choice==2:
            timeline_loop_transmissions(a_choice, t_choice)
        elif choice==3:
            gender_loop_transmissions(a_choice, t_choice)
        elif choice==4:
            agegroup_loop_transmissions(a_choice, t_choice)
        elif choice==5:
            occupation_loop_transmissions(a_choice, t_choice)
        elif choice==6:
            allTransmissions()
        elif choice==7:
             combinedFilter_loop_recovered()
        elif choice==8:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")

    return 


def weekly_testing_loop():

    while True:
        weekly_testing_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(weeklyTesting_options)))

        if choice==1:
            region_testing_loop()
        elif choice==2:
            timeline_testing_loop()
        elif choice==3:
            regionAndTimeline_loop()
        elif choice==4:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return

def reporting_loop():

    while True:
        print("Region")
        for i, option in enumerate(region_options[:-1]):
            print("\t%s)" % (i+1), option)
        regionChoice = int(input("Enter your choice [1-%d]: " % (len(region_options)-1)))

        print("Timeline")
        for i, option in enumerate(timeline_options[:-1]):
            print("\t%s)" % (i+1), option)
        timeLineChoice = int(input("Enter your choice [1-%d]: " % (len(timeline_options)-1)))

        print("Gender")
        for i, option in enumerate(gender_options[:-1]):
            print("\t%s)" % (i+1), option)
        genderChoice = int(input("Enter your choice [1-%d]: " % (len(gender_options)-1)))

        print("Age Group")
        for i, option in enumerate(ageGroup_options[:-1]):
            print("\t%s)" % (i+1), option)
        ageGroupChoice = int(input("Enter your choice [1-%d]: " % (len(ageGroup_options)-1)))

        print("Occupation")
        for i, option in enumerate(occupation_options[:-1]):
            print("\t%s)" % (i+1), option)
        occupationChoice = int(input("Enter your choice [1-%d]: " % (len(occupation_options)-1)))

        print("Did the patient recover or did they die or are they currently infected?")
        for i, option in enumerate(recovered_or_died_options):
            print("\t%s)" % (i+1), option)
        currentStatus = int(input("Enter your choice [1-%d]: " % (len(occupation_options)-1)))

        # Insert into Background information
        insertQuery = "INSERT INTO BackgroundInfo (region, episodeWeek, gender, ageGroup, occupation) VALUES (%d, %d, %d, %d, %d)" % (regionChoice, timeLineChoice+35, genderChoice, ageGroupChoice, occupationChoice)
        # print(insertQuery)
        cursor.execute(insertQuery)
        caseID = cursor.lastrowid
        # print(caseID)

        if currentStatus == 1 or currentStatus == 2:
            print("Hospital Status")
            for i, option in enumerate(hospitalization_options[:-1]):
                print("\t%s)" % (i+1), option)
            hospitalizationChoice = int(input("Enter your choice [1-%d]: " % (len(hospitalization_options)-1)))

            if currentStatus == 1: # Insert into recovered table
                insertRecoveredQuery = "INSERT INTO Recovered (caseID, hospitalStatus, episodeWeek) VALUES (%d, %d, %d)" % (caseID, hospitalizationChoice,99)
                # print(insertRecoveredQuery)
                cursor.execute(insertRecoveredQuery)
            elif currentStatus == 2: # Insert into deaths table
                insertDeathQuery = "INSERT INTO Deaths (caseID, hospitalStatus) VALUES (%d, %d)" % (caseID, hospitalizationChoice)
                # print(insertDeathQuery)
                cursor.execute(insertDeathQuery)

        # Save all changes to the database
        print("COVID-19 case reported successfully!")
        mydb.commit()

        choice = input("Would you like to report another case [y/n]: ")

        if choice == 'N' or choice == 'n' or choice == 'No' or choice == 'no':
            break
        elif choice == 'Y' or choice == 'y' or choice == 'Yes' or choice == 'yes':
            continue
        else:
            input("Wrong option selection. Enter any key to try again..")

    return    

#### Main Code ####
home_screen_menu()

while mainLoop:          
    print_menu()    ## Displays menu
    choice = int(input("Enter your choice [1-%d]: " % len(main_options)))
    
    if choice==1:     
        general_information_loop()
    elif choice==2:
        death_loop()
    elif choice==3:
        recovered_loop()
    elif choice==4:
        transmissions_loop_asymptomatic()
    elif choice==5:
        weekly_testing_loop()
    elif choice==6:
        reporting_loop()
    elif choice==7:
        print("Goodbye!")
        mainLoop=False
    else:
        input("Wrong option selection. Enter any key to try again..")