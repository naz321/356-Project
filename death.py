from menu import *

def region_loop_death():
    while True:
        region_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(region_options)))

        if choice==1:
            print(1)
        elif choice==2:
            print(2)
        elif choice==3:
            print(3)
        elif choice==4:
            print(4)
        elif choice==5:
            print(5)
        elif choice==6:
            print(6)
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return 

def timeline_loop_death():
    while True:
        timeline_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(timeline_options)))

        if choice==1:
            print(1)
        elif choice==2:
            print(2)
        elif choice==3:
            print(3)
        elif choice==4:
            print(4)
        elif choice==5:
            print(5)
        elif choice==6:
            print(6)
        elif choice==7:
            print(7)
        elif choice==8:
            print(8)
        elif choice==9:
            print(9)
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return 

def gender_loop_death():
    while True:
        gender_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(gender_options)))

        if choice==1:
            print(1)
        elif choice==2:
            print(2)
        elif choice==3:
            print(3)
        elif choice==4:
            print(4)
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return

def agegroup_loop_death():
    while True:
        ageGroup_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(ageGroup_Options)))

        if choice==1:
            print(1)
        elif choice==2:
            print(2)
        elif choice==3:
            print(3)
        elif choice==4:
            print(4)
        elif choice==5:
            print(5)
        elif choice==6:
            print(6)
        elif choice==7:
            print(7)
        elif choice==8:
            print(8)
        elif choice==9:
            print(9)
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return

def occupation_loop_death():
    while True:
        occupation_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(occupation_options)))

        if choice==1:
            print(1)
        elif choice==2:
            print(2)
        elif choice==3:
            print(3)
        elif choice==4:
            print(4)
        elif choice==5:
            print(5)
        elif choice==6:
            print(6)
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return

def hospitalization_loop_death():
    while True:
        hospitalization_menu()
        choice = int(input("Enter your choice [1-%d]: " % len(hospitalization_options)))

        if choice==1:
            print(1)
        elif choice==2:
            print(2)
        elif choice==3:
            print(3)
        elif choice==4:
            break
        else:
            input("Wrong option selection. Enter any key to try again..")
    
    return

def allDeaths():
    print("All deaths")
    
def combinedFilter_loop_death():
    print("Combined Filter")