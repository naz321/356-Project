from mysqlInformation import *

# Regular Options
main_options = ["Confirmed COVID-19 Cases", "Deaths From COVID-19", "Recovered From COVID-19", "Transmission", "COVID-19 Testing", "Report a new case of COVID-19", "Add a new location", "Government Login", "Exit"]
background_information_options = ["Region", "Timeline", "Gender", "Age Group", "Occupation", "More than 1 Filter", "Go Back"]
death_options = ["Region", "Timeline", "Gender", "Age Group", "Occupation", "Hospitalization", "All Deaths", "More than 1 Filter", "Go Back"]
recovered_options = ["Region", "Timeline", "Gender", "Age Group", "Occupation", "Hospitalization", "All Recovered", "More than 1 Filter", "Go Back"]
region_options = ["Atlantic (New Brunswick, Nova Scotia, Prince Edward Island, Newfoundland and Labrador)", "Quebec", "Ontario and Nunavut", "Prairies (Alberta, Saskatchewan, Manitoba, Northwest Territories)", "Northwest Territories (British Columbia, Yukon)", "Go Back"]
timeline_options = ["Week 36 (Week of September 6th)", "Week 37 (Week of September 13th)", "Week 38 (Week of September 20th)", "Week 39 (Week of September 27th)", "Week 40 (Week of October 4th)", "Week 41 (Week of October 11th)", "Week 42 (Week of October 18th)", "Week 43 (Week of October 25th)", "Go Back"]
gender_options = ["Male", "Female", "Not Stated/Other", "Go Back"]
ageGroup_options = ["0-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80+", "Go back"]
occupation_options = ["Health Care Workers", "School or daycare workers", "Long term care residents", "Other", "Not Stated", "Go Back"]
hospitalization_options = ["Hospitalized (ICU)", "Hospitalized (Non-ICU)", "Non-Hospitalized", "Not stated", "Go Back"]
weeklyTesting_options = ["Region", "Timeline", "Region and Timeline", "Go Back"]
transmissions_options = ["Region", "Timeline", "Gender", "Age group", "Occupation", "All Transmissions", "More than 1 filter", "Go Back"]
asymptomatic_options = ["Yes", "No", "Don't care", "Go Back"]
transmissions_type_options = ["Contact of COVID Case", "Internation Travel", "Don't Care", "Go Back"]
recovered_or_died_options = ["Recovered", "Died", "Currently Infected"]
update_or_delete_options = ["Update Data", "Delete Data"]

# Combined Filter Options
region_options_all = ["Atlantic (New Brunswick, Nova Scotia, Prince Edward Island, Newfoundland and Labrador)", "Quebec", "Ontario and Nunavut", "Prairies (Alberta, Saskatchewan, Manitoba, Northwest Territories)", "Northwest Territories (British Columbia, Yukon)", "All"]
timeline_options_all = ["Week 36 (Week of September 6th)", "Week 37 (Week of September 13th)", "Week 38 (Week of September 20th)", "Week 39 (Week of September 27th)", "Week 40 (Week of October 4th)", "Week 41 (Week of October 11th)", "Week 42 (Week of October 18th)", "Week 43 (Week of October 25th)", "All"]
gender_options_all = ["Male", "Female", "Not Stated/Other", "All"]
ageGroup_options_all = ["0-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80+", "All"]
occupation_options_all = ["Health Care Workers", "School or daycare workers", "Long term care residents", "Other", "Not Stated", "All"]

def inputPrompt(options, maxValue):
    while True:
        try:
            choice = int(input("Enter your choice [1-%d]: " % len(options)))

            if not (checkInput(maxValue, choice)):
                input("Wrong option selection. Enter any key to try again..")
            else:
                return choice
        except ValueError:  
            input("Wrong option selection. Enter any key to try again..")


def checkInput(maxValue, choice):
    if choice > 0 and choice <= maxValue:
        return True
    else:
        return False

def home_screen_menu():
    print (24 * "-" , "COVID-19 Project" , 24 * "-")
    print ("Group 23")
    print ("By: Matthew Tang, Selina Ali, Naziba Haider")

def print_menu():
    print (30 * "-" , "MENU" , 30 * "-")
    for i, option in enumerate(main_options):
        print("%s)" % (i+1), option)
    print (67 * "-")

def general_information_menu():      
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose a Filter")
    for i, option in enumerate(background_information_options):
        print("%s)" % (i+1), option)
    print (67 * "-")

def asymptomatic_menu():      
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose if asymptomatic")
    for i, option in enumerate(asymptomatic_options):
        print("%s)" % (i+1), option)
    print (67 * "-")

def transmissions_type_menu():      
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose Transmission Type")
    for i, option in enumerate(transmissions_type_options):
        print("%s)" % (i+1), option)
    print (67 * "-")

def getNewRegionOptions():
    cursor.execute("SELECT CONCAT(groupName,' ','(', provinces ,')') FROM Location;") 
    result = cursor.fetchall()
    regionOptions =  [row[0] for row in result]
    regionOptions.append("Go Back") 
    return regionOptions

def region_menu():
    newRegionOptionsFromDb = getNewRegionOptions()   
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose a Region")
    for i, option in enumerate(newRegionOptionsFromDb):
        print("%s)" % (i+1), option)
    print (67 * "-")

def timeline_menu():      
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose a Timeline")
    for i, option in enumerate(timeline_options):
        print("%s)" % (i+1), option)
    print (67 * "-")

def gender_menu():      
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose a Gender")
    for i, option in enumerate(gender_options):
        print("%s)" % (i+1), option)
    print (67 * "-")

def ageGroup_menu():      
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose an Age Group")
    for i, option in enumerate(ageGroup_options):
        print("%s)" % (i+1), option)
    print (67 * "-")

def occupation_menu():      
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose an Occupation")
    for i, option in enumerate(occupation_options):
        print("%s)" % (i+1), option)
    print (67 * "-")

def hospitalization_menu():
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose a Status")
    for i, option in enumerate(hospitalization_options):
        print("%s)" % (i+1), option)
    print (67 * "-")

def death_menu():      
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose a Filter")
    for i, option in enumerate(death_options):
        print("%s)" % (i+1), option)
    print (67 * "-")

def recovered_menu():      
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose a Filter")
    for i, option in enumerate(recovered_options):
        print("%s)" % (i+1), option)
    print (67 * "-")

def transmissions_menu():      
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose a Filter")
    for i, option in enumerate(transmissions_options):
        print("%s)" % (i+1), option)
    print (67 * "-")

def weekly_testing_menu():       
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose a Filter")
    for i, option in enumerate(weeklyTesting_options):
        print("%s)" % (i+1), option)
    print (67 * "-")

def recovered_or_died_menu():
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose a Filter")
    for i, option in enumerate(recovered_or_died_options):
        print("%s)" % (i+1), option)
    print (67 * "-")

def combinedFilter_menu():
    print("combined Filter")
    # print (30 * "-" , "MENU" , 30 * "-")

    # print("1) Region")
    # for i, option in enumerate(region_options):
    #     print("\t" + chr(ord('a') + i) + ")\t" + option)

    # print("2) Timeline")
    # for i, option in enumerate(timeline_options):
    #     print("\t" + chr(ord('a') + i) + ")\t" + option)
    
    # print("3) Gender")
    # for i, option in enumerate(gender_options):
    #     print("\t" + chr(ord('a') + i) + ")\t" + option)

    # print("4) Age Group")
    # for i, option in enumerate(ageGroup_options):
    #     print("\t" + chr(ord('a') + i) + ")\t" + option)

    # print("5) Occupation")
    # for i, option in enumerate(occupation_options):
    #     print("\t" + chr(ord('a') + i) + ")\t" + option)

    # print (67 * "-")

def updateData(caseId):
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

    print("Did the patient recover or did they die or are they currently infected?")
    for i, option in enumerate(recovered_or_died_options):
        print("\t%s)" % (i+1), option)
    currentStatus = inputPrompt(recovered_or_died_options, len(recovered_or_died_options))

    if currentStatus == 1 or currentStatus == 2:
        print("Hospital Status")
        for i, option in enumerate(hospitalization_options[:-1]):
            print("\t%s)" % (i+1), option)
        hospitalizationChoice = inputPrompt(hospitalization_options[:-1], len(hospitalization_options)-1)

        if currentStatus == 1: # Insert into recovered table
            updateRecoveredQuery = "UPDATE Recovered SET hospitalStatus = %d WHERE caseID = %d" % (hospitalizationChoice, caseId)
            # print(insertRecoveredQuery)
            cursor.execute(updateRecoveredQuery)
        elif currentStatus == 2: # Insert into deaths table
            updateDeathQuery = "UPDATE Deaths SET hospitalStatus = %d WHERE caseID = %d" % (hospitalizationChoice, caseId)
            # print(insertDeathQuery)
            cursor.execute(updateDeathQuery)
    
    # Save all changes to the database
    print("Record successfully updated!")
    mydb.commit()

def deleteData(caseId):
    print("Did the patient recover or did they die or are they currently infected?")
    for i, option in enumerate(recovered_or_died_options):
        print("\t%s)" % (i+1), option)
    currentStatus = inputPrompt(recovered_or_died_options, len(recovered_or_died_options))

    # Delete children first because of Fk reference
    if currentStatus == 1:
        deleteRecoveredQuery = "DELETE FROM Recovered WHERE caseID = %d" % caseId
        cursor.execute(deleteRecoveredQuery)
    elif currentStatus == 2:
        deleteDeathQuery = "DELETE FROM Deaths WHERE caseID = %d" % caseId
        cursor.execute(deleteDeathQuery)
    
    # Delete from Background information
    deleteFromTransmissionsQuery = "DELETE FROM Transmissions WHERE caseID = %d" % caseId
    cursor.execute(deleteFromTransmissionsQuery)
    deleteBackgroundInfoQuery = "DELETE FROM BackgroundInfo WHERE caseID = %d" % caseId
    cursor.execute(deleteBackgroundInfoQuery)

    print("Record successfully deleted!")
    mydb.commit()