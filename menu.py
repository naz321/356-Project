# Regular Options
main_options = ["Confirmed COVID-19 Cases", "Deaths", "Recovered", "Transmission", "COVID-19 Testing", "Report a case of COVID-19", "Exit"]
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

# Combined Filter Options
region_options_all = ["Atlantic (New Brunswick, Nova Scotia, Prince Edward Island, Newfoundland and Labrador)", "Quebec", "Ontario and Nunavut", "Prairies (Alberta, Saskatchewan, Manitoba, Northwest Territories)", "Northwest Territories (British Columbia, Yukon)", "All"]
timeline_options_all = ["Week 36 (Week of September 6th)", "Week 37 (Week of September 13th)", "Week 38 (Week of September 20th)", "Week 39 (Week of September 27th)", "Week 40 (Week of October 4th)", "Week 41 (Week of October 11th)", "Week 42 (Week of October 18th)", "Week 43 (Week of October 25th)", "All"]
gender_options_all = ["Male", "Female", "Not Stated/Other", "All"]
ageGroup_options_all = ["0-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80+", "All"]
occupation_options_all = ["Health Care Workers", "School or daycare workers", "Long term care residents", "Other", "Not Stated", "All"]

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

def region_menu():      
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose a Region")
    for i, option in enumerate(region_options):
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