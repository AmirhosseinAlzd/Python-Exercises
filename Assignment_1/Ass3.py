import os

side_1=float(input('side 1 = ')) 
side_2=float(input('side 2 = '))
side_3=float(input('side 3 = '))

while side_1 <= 0 or side_2 <= 0 or side_3 <= 0:
    os.system("clear")
    side_1 = float(input('Error !! Enter possitive numbers for sides  =  '))
    side_2=float(input('side 2 = '))
    side_3=float(input('side 3 = '))

if side_1 >= (side_2 + side_3) or side_2 >= (side_1 + side_3) or side_3 >= (side_2 + side_1) :
    can_triangle = False
else :
    can_triangle = True


if can_triangle == True :
    print('Possible')
else :
    print('Impossible')