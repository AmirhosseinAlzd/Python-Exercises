while True :
    Second = int(input('Enter Your Second(s): '))
    while Second < 0:
        seconds = int(input('Error !\n\tPlz Enter posetive Number : '))

    Seconds = Second
    Hour = int(Second / 3600)
    Second = Second % 3600
    Minute = int(Second / 60)
    Second = Second % 60

    print(Seconds,"s  is/are ",Hour,"h  ",Minute,"m  ",Second,"s")

    Condition_for_Continue = int(input("\n1- Continue\n2- Exit\n\n"))
    if Condition_for_Continue == 2 :
        exit(0)