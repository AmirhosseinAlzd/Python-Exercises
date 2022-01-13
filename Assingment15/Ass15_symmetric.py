from math import *
Array = []
while True :
    num = input('\nenter your number : for chel your number enter x\n\t')
    if num == 'x' :
        break
    else :
        Array.append(int(num))
print(Array)


def isSymmetric(Array):
    for i in range(0, floor(len(Array)/2)):
        if Array[i] == Array [len(Array)-(i+1)]:
            continue
        else :
            return False
    return True

if (isSymmetric(Array)):
    print ("Yes")
else:
    print ("No")