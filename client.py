from menu import *
from generalInformation import *
from death import *
from recovered import *
from weeklyTesting import *
from transmissions import *

def general_information_loop():

    while True:
        general_information_menu()
        choice = inputPrompt(background_information_options, len(background_information_options))
        
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
    
    return

def death_loop():

    while True:
        death_menu()
        choice = inputPrompt(death_options, len(death_options))

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
    
    return

def recovered_loop():

    while True:
        recovered_menu()
        choice = inputPrompt(recovered_options, len(recovered_options))

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
        asymptomatic_choice = inputPrompt(asymptomatic_options, len(asymptomatic_options))

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
        transmission_type_choice = inputPrompt(transmissions_type_options, len(transmissions_type_options))

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
        choice = inputPrompt(transmissions_options, len(transmissions_options))

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
        choice = inputPrompt(weeklyTesting_options, len(weeklyTesting_options))

        if choice==1:
            region_testing_loop()
        elif choice==2:
            timeline_testing_loop()
        elif choice==3:
            regionAndTimeline_loop()
        elif choice==4:
            break

    return

def reporting_loop():

    while True:
        print("Region")
        newRegionOptionsFromDb = getNewRegionOptions()   
        for i, option in enumerate(newRegionOptionsFromDb[:-1]):
            print("\t%s)" % (i+1), option)
        regionChoice = inputPrompt(newRegionOptionsFromDb[:-1], len(newRegionOptionsFromDb)-1)

        print("Timeline")
        for i, option in enumerate(timeline_options[:-1]):
            print("\t%s)" % (i+1), option)
        timeLineChoice = inputPrompt(timeline_options[:-1], len(timeline_options)-1)

        print("Gender")
        for i, option in enumerate(gender_options[:-1]):
            print("\t%s)" % (i+1), option)
        genderChoice = inputPrompt(gender_options[:-1], len(gender_options)-1)
        if genderChoice == 3: # change non stated/other
            genderChoice = 9

        print("Age Group")
        for i, option in enumerate(ageGroup_options[:-1]):
            print("\t%s)" % (i+1), option)
        ageGroupChoice = inputPrompt(ageGroup_options[:-1], len(ageGroup_options)-1)

        print("Occupation")
        for i, option in enumerate(occupation_options[:-1]):
            print("\t%s)" % (i+1), option)
        occupationChoice = inputPrompt(occupation_options[:-1], len(occupation_options)-1)
        if occupationChoice == 5: # change not stated
            occupationChoice = 9

        print("Did the patient recover or did they die or are they currently infected?")
        for i, option in enumerate(recovered_or_died_options):
            print("\t%s)" % (i+1), option)
        currentStatus = inputPrompt(recovered_or_died_options, len(recovered_or_died_options))

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
            hospitalizationChoice = inputPrompt(hospitalization_options[:-1], len(hospitalization_options)-1)

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

def new_location_loop():

    while True:
        
        while True:
            city = input("Enter city name: ")
            if city == '':
                input("Invalid Input. Enter any key to try again..")
            else:
                break
        
        while True:
            province = input("Enter province: ")
            if province == '':
                input("Invalid Input. Enter any key to try again..")
            else:
                break

        cursor.execute("SELECT MAX(region) FROM Location")
        regionID = cursor.fetchone()[0]
        # print(regionID)
        # Insert into Location Table
        insertQuery = "INSERT INTO Location (region, groupName, provinces) VALUES (%d, '%s', '%s')" % (regionID+1, city, province)
        # print(insertQuery)
        cursor.execute(insertQuery)

        # Save all changes to the database
        print("City successfully added!")
        mydb.commit()

        # Add changes to new list
        region_options.insert(-1, "%s (%s)" %(city, province))

        choice = input("Would you like to report another case [y/n]: ")

        if choice == 'N' or choice == 'n' or choice == 'No' or choice == 'no':
            break
        elif choice == 'Y' or choice == 'y' or choice == 'Yes' or choice == 'yes':
            continue
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return    

def edit_data_loop():
    print("A government account can edit data... Please Login")
    login = input("Login: ")
    password = input("Password: ") 
    
    if not(login == "root" and password == "root"):
        print("Wrong login or password")
        return

    # check if they want to edit data
    while True:
        choice = input("Would you like to edit data [y/n]: ")

        if choice == 'N' or choice == 'n' or choice == 'No' or choice == 'no':
            return 

        # find a valid caseId
        cursor.execute("SELECT MAX(caseID) FROM BackgroundInfo")
        maxCaseId = cursor.fetchone()[0]
        caseId = 1
        while True:
            try:
                caseId = int(input("Enter a caseId: "))
                if caseId > maxCaseId or caseId <= 0:
                    input("Invalid option selection. Enter any key to try again..")
                    continue
                else:
                    break
            except ValueError:
                input("Invalid option selection. Enter any key to try again..")

        print("Region")
        newRegionOptionsFromDb = getNewRegionOptions()   
        for i, option in enumerate(newRegionOptionsFromDb[:-1]):
            print("\t%s)" % (i+1), option)
        regionChoice = inputPrompt(newRegionOptionsFromDb[:-1], len(newRegionOptionsFromDb)-1)

        print("Timeline")
        for i, option in enumerate(timeline_options[:-1]):
            print("\t%s)" % (i+1), option)
        timeLineChoice = inputPrompt(timeline_options[:-1], len(timeline_options)-1)

        print("Gender")
        for i, option in enumerate(gender_options[:-1]):
            print("\t%s)" % (i+1), option)
        genderChoice = inputPrompt(gender_options[:-1], len(gender_options)-1)
        if genderChoice == 3: # change non stated/other
            genderChoice = 9

        print("Age Group")
        for i, option in enumerate(ageGroup_options[:-1]):
            print("\t%s)" % (i+1), option)
        ageGroupChoice = inputPrompt(ageGroup_options[:-1], len(ageGroup_options)-1)

        print("Occupation")
        for i, option in enumerate(occupation_options[:-1]):
            print("\t%s)" % (i+1), option)
        occupationChoice = inputPrompt(occupation_options[:-1], len(occupation_options)-1)
        if occupationChoice == 5: # change not stated
            occupationChoice = 9

        updateQuery = "UPDATE BackgroundInfo SET region = %d, episodeWeek = %d, gender = %d, ageGroup = %d, occupation = %d WHERE caseID = %d" % (regionChoice, timeLineChoice+35, genderChoice, ageGroupChoice, occupationChoice, caseId)
        # print(updateQuery)

        cursor.execute(updateQuery)

        # Save all changes to the database
        print("Record successfully updated!")
        mydb.commit()

#### Main Code ####
home_screen_menu()

def main():
    while True:          
        print_menu()    ## Displays menu
        choice = inputPrompt(main_options, len(main_options))

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
            new_location_loop()
        elif choice==8:
            edit_data_loop()
        elif choice==9:
            print("Goodbye!")
            break

main()