from os import system

from termcolor import colored

class fraction:
    def __init__(self , a , b , c , d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def sum(self) :
        num = (self.a*self.d)+(self.c*self.b)
        den = self.b*self.d
        return str( str(num) + '/' + str(den) )
    def sub(self) :
        num = (self.a*self.d)-(self.c*self.b)
        den = self.b*self.d
        return str( str(num) + '/' + str(den) )
    def mul(self):
        num = self.a*self.c
        den = self.b*self.d
        return str( str(num) + '/' + str(den) )
    def div(self) :
        num = self.a*self.d
        den = self.b*self.c
        return str( str(num) + '/' + str(den) )

print('Fraction 1 :\n')
a = int(input('\n\tEnter numerator   : '))
b = int(input('\n\tEnter denominator : '))
print('\n\nFraction 2 :\n')
c = int(input('\n\tEnter numerator   : '))
d = int(input('\n\tEnter denominator : '))
while a == 0 or b == 0 or c == 0  or  d == 0 :
    system('clear')
    print(colored('\nPlz dont Enter 0 \n\n' , 'red'))
    print('Fraction 1 :\n')
    a = int(input('\n\tEnter numerator   : '))
    b = int(input('\n\tEnter denominator : '))
    print('\n\nFraction 2 :\n')
    c = int(input('\n\tEnter numerator   : '))
    d = int(input('\n\tEnter denominator : '))

fr = fraction(a,b,c,d)

while True :
    system('clear')
    print('╒══════════════════════════════════════════════╕')
    print('│         ⟹  ➊ - Add                           │')
    print('│         ⟹  ➋ - Subtract                      │')
    print('│         ⟹  ➌ - Multiplication                │')
    print('│         ⟹  ➍ - Division                      │')
    print('│         ⟹  ➎ - Exit                          │')
    print('╘══════════════════════════════════════════════╛\n')

    choose_char = input('Plz choose one of them :  ')
    match choose_char :
        case '1' :
            system('clear')
            print('\n\t Sum ==> ' , fr.a , '/' , fr.b ,'  +  ',fr.c , '/' , fr.d , ' = ' , fr.sum())
            p = input()    
        case '2':
            system('clear')
            print('\n\t Sub ==> ' , fr.a , '/' , fr.b ,'  -  ',fr.c , '/' , fr.d , ' = ' , fr.sub())
            p = input()
        case '3':
            system('clear')
            print('\n\t Mul ==> ' , fr.a , '/' , fr.b ,'  *  ',fr.c , '/' , fr.d , ' = ' , fr.mul())
            p = input()
        case '4':
            system('clear')
            print('\n\t Div ==> ' , fr.a , '/' , fr.b ,'  /  ',fr.c , '/' , fr.d , ' = ' , fr.div())
            p = input()
        case '5':
            system('clear')
            exit(0)