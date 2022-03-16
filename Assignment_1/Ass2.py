import math
import os
radius = float(input('Enter radius =  '))
while radius < 0 :
    os.system("clear")
    radius = float(input('Error !! Enter Non-negative numbers for radius  =  '))
Area = (math.pi)*(radius**2)
Environment = 2*math.pi*radius
print('Area = ' , Area)
print('Environment = ' , Environment)