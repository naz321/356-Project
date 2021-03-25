from menu import *
from generalInformation import *
from weeklyTesting import *

## Text menu in Python

### Global variables
mainLoop=True
generalInformationLoop=True
weeklyTestingLoop=True

def general_information_loop():

    while generalInformationLoop:
        general_information_menu()
        choice = int(input("Enter your choice [1-7]: "))

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

def weekly_testing_loop():

    while weeklyTestingLoop:
        weekly_testing_menu()
        choice = int(input("Enter your choice [1-4]: "))

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
    choice = int(input("Enter your choice [1-6]: "))
    
    if choice==1:     
        general_information_loop()
    elif choice==2:
        print(2)
    elif choice==3:
        print(3)
    elif choice==4:
        print(4)
    elif choice==5:
        weekly_testing_loop()
    elif choice==6:
        print("Goodbye!")
        mainLoop=False
    else:
        input("Wrong option selection. Enter any key to try again..")