main_options = ["Confirmed COVID-19 Cases", "Deaths", "Recovered", "Transmission", "COVID-19 Testing", "Exit"]
background_information_options = ["Region", "Timeline", "Gender", "Age Group", "Occupation", "More than 1 Filter", "Go Back"]
death_options = ["Region", "Timeline", "Gender", "Age Group", "Occupation", "Hospitalization", "All Deaths", "More than 1 Filter", "Go Back"]
recovered_options = ["Region", "Timeline", "Gender", "Age Group", "Occupation", "Hospitalization", "All Recovered", "More than 1 Filter", "Go Back"]
region_options = ["Atlantic (New Brunswick, Nova Scotia, Prince Edward Island, Newfoundland and Labrador)", "Quebec", "Ontario and Nunavut", "Prairies (Alberta, Saskatchewan, Manitoba, Northwest Territories)", "Northwest Territories (British Columbia, Yukon)", "Go Back"]
timeline_options = ["Week 36 (Week of September 6th)", "Week 37 (Week of September 13th)", "Week 38 (Week of September 20th)", "Week 39 (Week of September 27th)", "Week 40 (Week of October 4th)", "Week 41 (Week of October 11th)", "Week 42 (Week of October 18th)", "Week 43 (Week of October 25th)", "Go Back"]
gender_options = ["Male", "Female", "Not Stated/Other", "Go Back"]
ageGroup_Options = ["0-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80+", "Go back"]
occupation_options = ["Health Care Workers", "School or daycare workers", "Long term care residents", "Other", "Not Stated", "Go Back"]
hospitalization_options = ["Hospitalized (ICU)", "Hospitalized (Non-ICU)", "Non-Hospitalized", "Go Back"]
weeklyTesting_options = ["Region", "Timeline", "Region and Timeline", "Go Back"]

def home_screen_menu():
    print (24 * "-" , "COVID-19 Project" , 24 * "-")
    print ("Group 23")
    print ("By: Matthew Tang, Selina Ali, Naziba Haider")

def print_menu():
    print (30 * "-" , "MENU" , 30 * "-")
    for i, option in enumerate(main_options):
        print(i+1, option)
    print (67 * "-")

def general_information_menu():      
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose a Filter")
    for i, option in enumerate(background_information_options):
        print(i+1, option)
    print (67 * "-")

def region_menu():      
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose a Region")
    for i, option in enumerate(region_options):
        print(i+1, option)
    print (67 * "-")

def timeline_menu():      
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose a Timeline")
    for i, option in enumerate(timeline_options):
        print(i+1, option)
    print (67 * "-")

def gender_menu():      
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose a Gender")
    for i, option in enumerate(gender_options):
        print(i+1, option)
    print (67 * "-")

def ageGroup_menu():      
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose an Age Group")
    for i, option in enumerate(ageGroup_Options):
        print(i+1, option)
    print (67 * "-")

def occupation_menu():      
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose an Occupation")
    for i, option in enumerate(occupation_options):
        print(i+1, option)
    print (67 * "-")

def hospitalization_menu():
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose a Status")
    for i, option in enumerate(hospitalization_options):
        print(i+1, option)
    print (67 * "-")

def death_menu():      
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose a Filter")
    for i, option in enumerate(death_options):
        print(i+1, option)
    print (67 * "-")

def recovered_menu():      
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose a Filter")
    for i, option in enumerate(recovered_options):
        print(i+1, option)
    print (67 * "-")

def weekly_testing_menu():       
    print (30 * "-" , "MENU" , 30 * "-")
    print ("Choose a Filter")
    for i, option in enumerate(weeklyTesting_options):
        print(i+1, option)
    print (67 * "-")