def Show_board(r  , c):
    print('\n\n')
    for i in range(r):
        print('\t\t\t\t\t\t' , end='')
        for j in range(c):
            if (i+j)%2 == 0:
                print('⬛' , end='')
            elif (i+j)%2 != 0:
                print('⬜' , end='')
        print()


Rows = int(input('Plz Enter the number of Rows :\n\t==> '))
Columns = int(input('\n\nPlz Enter the number of Columns :\n\t==> '))

Show_board(Rows , Columns )
print('\n\n')
