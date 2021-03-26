from menu import *
from generalInformation import *
from death import *
from recovered import *
from weeklyTesting import *

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
        print(4)
    elif choice==5:
        weekly_testing_loop()
    elif choice==6:
        print("Goodbye!")
        mainLoop=False
    else:
        input("Wrong option selection. Enter any key to try again..")