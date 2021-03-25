from menu import *

def region_testing_loop():
    while True:
        region_menu()
        choice = int(input("Enter your choice [1-6]: "))

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

def timeline_testing_loop():
    while True:
        timeline_menu()
        choice = int(input("Enter your choice [1-9]: "))

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

def regionAndTimeline_loop():
    print("Region and Timeline")