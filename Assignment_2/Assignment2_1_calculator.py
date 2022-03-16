import math

Operation = 'q'
while(Operation != 'e'):
    Operation = input("\n\nWhich Operation Do You Want to Choose? \n  + (Add)\n  - (Subtrack)\n  * (Multiply)\n  / (Divide)"
                  "\n  # (Advanced)\n  e (Exit)\n\n")
    if(Operation=='+'):
        Number_1 = float(input("Enter your first number : "))
        Number_2 = float(input("Enter your second number : "))
        print(Number_1 ," + " ,Number_2 ," = " ,Number_1 + Number_2) 
    elif(Operation=='-'):
        Number_1 = float(input("Enter your first number : "))
        Number_2 = float(input("Enter your second number : "))
        print(Number_1 ," - " ,Number_2 ," = " ,Number_1 - Number_2)
    elif(Operation=='*'):
        Number_1 = float(input("Enter your first number : "))
        Number_2 = float(input("Enter your second number : "))
        print(Number_1 ," * " ,Number_2 ," = " ,Number_1 * Number_2)
    elif(Operation=='/'):
        Number_1 = float(input("Enter your first number : "))
        Number_2 = float(input("Enter your second number : "))
        while Number_2 == 0:
            Number_2 = float(input("Error !\n\tYour second number must not be 0  , Enter again : "))
        print(Number_1 ," / " ,Number_2 ," = " ,Number_1 / Number_2)

    elif(Operation=='#'):
        Operation = input("Which Advanced Operation Do You Want to Choose? \n  log (Logaritm)\n  Sin\n  Cos\n  Tan\n  Cot\n  b  (back)\n\n")

        if(Operation=='log'):
            Number_1 = float(input("Enter your number :"))
            while Number_1<0 or Number_1==0 :
                Number_1 = float(input("Error !\n\tPlz Enter Positive Number :"))
            print("Log( ",Number_1," ) = ",math.log(Number_1))           
        elif(Operation=='Sin' or Operation=='sin'):
            Number_1 = float(input("Enter your degrees :"))
            print("Sin( ",Number_1," ) = ",math.sin(math.radians(Number_1)))
        elif(Operation=='Cos' or Operation=='cos'):
            Number_1 = float(input("Enter your degrees :"))
            print("Cos( ",Number_1," ) = ",math.cos(math.radians(Number_1)))
        elif(Operation=='Tan' or Operation=='tan'):
            Number_1 = float(input("Enter your degrees :"))
            print("Tan( ",Number_1," ) = ",math.tan(math.radians(Number_1)))
        elif(Operation=='Cot' or Operation=='cot'):
            Number_1 = float(input("Enter your degrees :"))
            print("Cot( ",Number_1," ) = ",1/math.tan(math.radians(Number_1)))
        elif(Operation=='b'):
            print("")
    elif(Operation=='e'):
        exit(0)

    else :
        print("incorrect input .... plz try again \n")





