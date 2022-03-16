from random import randint
from typing import Counter
#1 = front
#2 = back

Counter_user = 0 
Counter1_computer= 0 
Counter2_computer = 0
while True :
    while Counter_user < 5 and Counter1_computer < 5 and Counter2_computer < 5 :
        Computer1_choice = randint(1,2)
        Computer2_choice = randint(1,2)
        User_choice = int(input("\nPlz choose one of them  :\n\t1- front\n\t2- back\n"))
        if User_choice == 1 and Computer1_choice == 1 and Computer2_choice == 1:
            Counter_user = 1 + Counter_user
            Counter1_computer = 1 + Counter1_computer
            Counter2_computer = 1 + Counter2_computer
            print ("\n\t\tYou   VS   Computer1   VS   Computer2\n\n\t\t ",Counter_user,"          ",Counter1_computer,"          ",Counter2_computer,"\n")
        elif User_choice == 2 and Computer1_choice == 2 and Computer2_choice == 2:
            Counter_user = 1 + Counter_user
            Counter1_computer = 1 + Counter1_computer
            Counter2_computer = 1 + Counter2_computer
            print ("\n\t\tYou   VS   Computer1   VS   Computer2\n\n\t\t ",Counter_user,"          ",Counter1_computer,"          ",Counter2_computer,"\n")
        
        elif User_choice == 1 and Computer1_choice == 2 and Computer2_choice == 2:
            Counter_user = 1 + Counter_user
            print ("\n\t\tYou   VS   Computer1   VS   Computer2\n\n\t\t ",Counter_user,"          ",Counter1_computer,"          ",Counter2_computer,"\n")

        elif User_choice == 2 and Computer1_choice == 1 and Computer2_choice == 1:
            Counter_user = 1 + Counter_user
            print ("\n\t\tYou   VS   Computer1   VS   Computer2\n\n\t\t ",Counter_user,"          ",Counter1_computer,"          ",Counter2_computer,"\n")

        elif User_choice == 2 and Computer1_choice == 1 and Computer2_choice == 2:
            Counter1_computer = 1 + Counter1_computer
            print ("\n\t\tYou   VS   Computer1   VS   Computer2\n\n\t\t ",Counter_user,"          ",Counter1_computer,"          ",Counter2_computer,"\n")

        elif User_choice == 1 and Computer1_choice == 2 and Computer2_choice == 1:
            Counter1_computer = 1 + Counter1_computer
            print ("\n\t\tYou   VS   Computer1   VS   Computer2\n\n\t\t ",Counter_user,"          ",Counter1_computer,"          ",Counter2_computer,"\n")

        elif User_choice == 2 and Computer1_choice == 2 and Computer2_choice == 1:
            Counter2_computer = 1 + Counter2_computer
            print ("\n\t\tYou   VS   Computer1   VS   Computer2\n\n\t\t ",Counter_user,"          ",Counter1_computer,"          ",Counter2_computer,"\n")

        elif User_choice == 1 and Computer1_choice == 1 and Computer2_choice == 2:
            Counter2_computer = 1 + Counter2_computer
            print ("\n\t\tYou   VS   Computer1   VS   Computer2\n\n\t\t ",Counter_user,"          ",Counter1_computer,"          ",Counter2_computer,"\n")
    
    if Counter_user == 5 :
            print("\n\n\t\tYou Win The Game ... \n")
    if Counter1_computer == 5 or Counter2_computer == 5:
            print("\n\n\t\tGame Over ... \n")
    Condition_for_Continue = int(input("\n1- Play again\n2- Exit\n\n"))
    if Condition_for_Continue == 2 :
        exit(0)