while True :
    Hour   = int(input('Enter the Hour: '))
    Minute = int(input('Enter the Minute: '))
    Second = int(input('Enter the Second: '))
        
    while Hour < 0 or Minute < 0 or Second < 0 or Minute >= 60 or Second >= 60:
        print('Error !\n\tEnter Positive Numbers and also Smaller than 60 for Minute and Second!')
        Hour   = int(input('Enter the Hour: '))
        Minute = int(input('Enter the Minute: '))
        Second = int(input('Enter the Second: '))


    print(Hour ,"h  " ,Minute,"m  ",Second,"s  is = ", Hour*3600 + Minute + Second , "s")

    Condition_for_Continue = int(input("\n1- Continue\n2- Exit\n\n"))
    if Condition_for_Continue == 2 :
        exit(0)