from os import system
class Time :
    def __init__(self , h =0  ,m = 0, s = 0 ):
        self.h = h
        self.m = m
        self.s = s
    def show(self):
        print(self.h , ':' , self.m , ':' , self.s)

    def fix_time(self):
        if self.s > 60 :
            self.s -=60
            self.m +=1
        if self.s < 0 :
            self.s = 60 + self.s
            self.m -=1
        if self.m > 60 :
            self.m -=60
            self.h +=1
        if self.m < 0 :
            self.m = 60 + self.m
            self.h -=1

    def sum(self , other):
        result = Time()
        result.h = self.h + other.h
        result.m = self.m + other.m
        result.s = self.s + other.s
        result.fix_time()
        return result
    def sub(self , other):
        result = Time()
        result.h = self.h - other.h
        result.m = self.m - other.m
        result.s = self.s - other.s
        result.fix_time()
        return result

    def show_time_to_sec(self):
        print(self.h ,"h  " ,self.m,"m  ",self.s,"s  is = ", self.h*3600 + self.m*60 + self.s , "s")
    def sec_to_time(self , Seconds):
        result = Time()
        result.h = int(Seconds/3600)
        result.s = Seconds%3600
        result.m = int(result.s/60)
        result.s = result.s%60
        return result




def input_value():
    Hour   = int(input('Enter the Hour: '))
    Minute= int(input('Enter the Minute: '))
    Second = int(input('Enter the Second: '))     
    while Hour < 0 or Minute < 0 or Second < 0 or Minute >= 60 or Second >= 60 :
        print('Error !\n\tEnter Positive Numbers and also Smaller than 60 for Minute and Second!')
        Hour   = int(input('Enter the Hour: '))
        Minute = int(input('Enter the Minute: '))
        Second = int(input('Enter the Second: '))
    return Hour,Minute,Second


while True :
    system('clear')
    print('╒══════════════════════════════════════════════╕')
    print('│         ⟹  ➊ - Sum                           │')
    print('│         ⟹  ➋ - Subtract                      │')
    print('│         ⟹  ➌ - Seconds to Time               │')
    print('│         ⟹  ➍ - Time to Seconds               │')
    print('│         ⟹  ➎ - Exit                          │')
    print('╘══════════════════════════════════════════════╛\n')

    choose_char = input('Plz choose one of them :  ')
    match choose_char :
        case '1' :
            system('clear')
            print('first time')
            h,m,s = input_value()
            t1 = Time(h,m,s)
            system('clear')
            print('second time')
            h,m,s = input_value()
            t2 = Time(h,m,s)
            system('clear')
            t1.show()
            print('                   +')
            t2.show()
            print('=====================')
            t3 = t1.sum(t2)
            t3.show()
            p = input()    
        case '2':
            system('clear')
            print('first time')
            h,m,s = input_value()
            t1 = Time(h,m,s)
            system('clear')
            print('second time')
            h,m,s = input_value()
            t2 = Time(h,m,s)
            system('clear')
            t1.show()
            print('                   -')
            t2.show()
            print('=====================')
            t3 = t1.sub(t2)
            t3.show()
            p = input()
        case '3':
            system('clear')
            seconds = int(input('Enter your seconds : '))
            t4 = Time()
            t4=t4.sec_to_time(seconds)
            t4.show()
            p = input()
        case '4':
            system('clear')
            h,m,s = input_value()
            t5 = Time(h,m,s)
            t5.show_time_to_sec()
            p = input()
        case '5':
            system('clear')
            exit(0)