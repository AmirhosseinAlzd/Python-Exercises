from random import randint
from typing import Counter
#1 = Rock
#2 = Paper
#3 = Scissors
Counter_user = 0 
Counter_computer = 0 
while True :
    while Counter_user < 5 and Counter_computer < 5 :
        Computer_choice = randint(1,3)
        User_choice = int(input("\nPlz choose one of them  :\n\t1- Rock\n\t2- Paper\n\t3- Scissors\n"))
        if User_choice == 1 and Computer_choice == 1 :
            Counter_user = 1 + Counter_user
            Counter_computer = 1 + Counter_computer
            print ("\n\t\tYou   VS   Computer\n\n\t\t ",Counter_user,"          ",Counter_computer,"\n")
        elif User_choice == 2 and Computer_choice == 2 :
            Counter_user = 1 + Counter_user
            Counter_computer = 1 + Counter_computer
            print ("\n\t\tYou   VS   Computer\n\n\t\t ",Counter_user,"          ",Counter_computer,"\n")
        elif User_choice == 3 and Computer_choice == 3 :
            Counter_user = 1 + Counter_user
            Counter_computer = 1 + Counter_computer
            print ("\n\t\tYou   VS   Computer\n\n\t\t ",Counter_user,"          ",Counter_computer,"\n")
        elif User_choice == 1 and Computer_choice == 2 :
            Counter_computer = 1 + Counter_computer
            print ("\n\t\tYou   VS   Computer\n\n\t\t ",Counter_user,"          ",Counter_computer,"\n")
        elif User_choice == 1 and Computer_choice == 3 :
            Counter_user = 1 + Counter_user
            print ("\n\t\tYou   VS   Computer\n\n\t\t ",Counter_user,"          ",Counter_computer,"\n")
        elif User_choice == 2 and Computer_choice == 1 :
            Counter_user = 1 + Counter_user
            print ("\n\t\tYou   VS   Computer\n\n\t\t ",Counter_user,"          ",Counter_computer,"\n")
        elif User_choice == 2 and Computer_choice == 3 :
            Counter_computer = 1 + Counter_computer
            print ("\n\t\tYou   VS   Computer\n\n\t\t ",Counter_user,"          ",Counter_computer,"\n")
        elif User_choice == 3 and Computer_choice == 1 :
            Counter_computer = 1 + Counter_computer
            print ("\n\t\tYou   VS   Computer\n\n\t\t ",Counter_user,"          ",Counter_computer,"\n")
        elif User_choice == 3 and Computer_choice == 2 :
            Counter_user = 1 + Counter_user
            print ("\n\t\tYou   VS   Computer\n\n\t\t ",Counter_user,"          ",Counter_computer,"\n")
        



    if Counter_user == 5 :
            print("\n\n\t\tYou Win The Game ... \n")
    if Counter_computer == 5 :
            print("\n\n\t\tGame Over ... \n")
    Condition_for_Continue = int(input("\n1- Play again\n2- Exit\n\n"))
    if Condition_for_Continue == 2 :
        exit(0)

