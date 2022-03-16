Number = int(input('Enter a Number to show it is a factoriel Number or not \n\t==> : '))
counter1 = fact = 1
while fact < Number:
    counter1 += 1
    fact *= counter1
if Number == fact:
    print('\n\t yes . it is a factoriel Number')
else:
    print('\n\t no . it is not a factoriel Number')