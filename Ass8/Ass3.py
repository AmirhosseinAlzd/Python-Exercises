from os import system


class ComplexNumbers:
    def init(self, complxNumber=0):
        self.complexNumber=complxNumber

    def addition(self, other):
        return ComplexNumbers(self.complexNumber + other.complexNumber)

    def subtract(self, other):
        return ComplexNumbers(self.complexNumber - other.complexNumber)

    def multiplication(self, other):
        return ComplexNumbers(self.complexNumber*other.complexNumber)

    def show(self):
        print(self.complexNumber,)

def print_Menu():
    system('clear')

    print('➊ - Addition')
    print('➋ - subtract')
    print('➌ - Multiplication')
    print('➍ - Exit')

    selected=int(input('\nPlease Choose your item : '))

    return(selected)



realNumber1=float(input('enter firdt real number : '))
imagNumber1=float(input('\nenter first imag number : '))
realNumber2=float(input('\nenter second real number : '))
imagNumber2=float(input('\nenter second imag number : '))


complexNumbers1=ComplexNumbers(complex(realNumber1, imagNumber1))
complexNumbers2=ComplexNumbers(complex(realNumber2, imagNumber2))
result=ComplexNumbers()


while True:
    select=print_Menu()

    match select:
        case 1:
            system('clear')
            result=complexNumbers1.addition(complexNumbers2)
            result.show()
            input()
        case 2:
            system('clear')
            result=complexNumbers1.subtract(complexNumbers2)
            result.show()
            input()
        case 3:
            system('clear')
            result=complexNumbers1.multiplication(complexNumbers2)
            result.show()
            input()
        case 4:
            break