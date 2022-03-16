from os import system
from termcolor import colored

from os import system
from termcolor import colored

def Show_table(r,c):
    for i in range(r):
        print('\t\t\t\t\t\t' , end='')
        for j in range(c):
            if i==0 or j==0 :
                print(colored((i+1)*(j+1) , 'red') , end='\t')
            else :
                print((i+1)*(j+1) , end='\t')
        print('\n')


Rows = int(input('Plz Enter the number of Rows :\n\t==> '))
Columns = int(input('\n\nPlz Enter the number of Columns :\n\t==> '))

Show_table(Rows , Columns )
print('\n\n')