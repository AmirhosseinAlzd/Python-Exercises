from os import system

from termcolor import colored

class Fraction :
    def __init__(self , s , m) :   # s = sorat  #m = makhraj
        self.s = s
        self.m = m
    def show(self):
        print(self.s,'/' , self.m)
    def mul(self ,other):    # self = kasre 1 ( khodesh)   #other = kasre 2
        soorat = self.s * other.s
        makhraj = self.m * other.m
        result = Fraction(soorat , makhraj)
        return result
    def div(self ,other):    # self = kasre 1 ( khodesh)   #other = kasre 2
        soorat = self.s * other.m
        makhraj = self.m * other.s
        result = Fraction(soorat , makhraj)
        return result
    def sum(self ,other):    # self = kasre 1 ( khodesh)   #other = kasre 2
        soorat = self.s * other.m + self.m * other.s
        makhraj = self.m * other.m
        result = Fraction(soorat , makhraj)
        return result
    def sub(self ,other):    # self = kasre 1 ( khodesh)   #other = kasre 2
        soorat = self.s * other.m - self.m * other.s
        makhraj = self.m * other.m
        result = Fraction(soorat , makhraj)
        return result

print('Fraction 1 :\n')
x1 = int(input('\n\tEnter numerator   : '))
x2 = int(input('\n\tEnter denominator : '))
print('\n\nFraction 2 :\n')
y1 = int(input('\n\tEnter numerator   : '))
y2 = int(input('\n\tEnter denominator : '))
while x1 == 0 or x2 == 0 or y1 == 0  or  y2 == 0 :
    system('clear')
    print(colored('\nPlz dont Enter 0 \n\n' , 'red'))
    print('Fraction 1 :\n')
    x1 = int(input('\n\tEnter numerator   : '))
    x2 = int(input('\n\tEnter denominator : '))
    print('\n\nFraction 2 :\n')
    y1 = int(input('\n\tEnter numerator   : '))
    y2 = int(input('\n\tEnter denominator : '))

a = Fraction(x1,x2)
b = Fraction(y1,y2)

while True :
    system('clear')
    print('╒══════════════════════════════════════════════╕')
    print('│         ⟹  ➊ - Sum                           │')
    print('│         ⟹  ➋ - Subtract                      │')
    print('│         ⟹  ➌ - Multiplication                │')
    print('│         ⟹  ➍ - Division                      │')
    print('│         ⟹  ➎ - Exit                          │')
    print('╘══════════════════════════════════════════════╛\n')

    choose_char = input('Plz choose one of them :  ')
    match choose_char :
        case '1' :
            system('clear')
            f = a.sum(b)
            print('\n\t Sum ==> ' , x1 , '/' , x2 ,'  +  ',y1 , '/' , y2 , ' = ' , end='')
            f.show()
            p = input()    
        case '2':
            system('clear')
            g = a.sub(b)
            print('\n\t Sum ==> ' , x1 , '/' , x2 ,'  -  ',y1 , '/' , y2 , ' = ' , end='')
            g.show()
        case '3':
            system('clear')
            c = a.mul(b)
            print('\n\t Sum ==> ' , x1 , '/' , x2 ,'  *  ',y1 , '/' , y2 , ' = ' , end='')
            c.show()
        case '4':
            system('clear')
            d = a.div(b)
            print('\n\t Sum ==> ' , x1 , '/' , x2 ,'  /  ',y1 , '/' , y2 , ' = ' , end='')
            d.show()
        case '5':
            system('clear')
            exit(0)
