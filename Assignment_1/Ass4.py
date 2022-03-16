weight = float(input('Enter your Weight (Kg) = '))
height = float(input('Enter your Height (m)  = '))
BMI = weight/(height**2)
print('Your BMI is : ' , BMI ,'\n')
if BMI <= 18.5 :
    print('Underweight')
elif BMI > 18.5 and BMI <= 24.99 :
    print('Normal')
elif BMI > 24.99 and BMI <= 29.99 :
    print('Overweight')
elif BMI > 30 and BMI <= 35 :
    print('Obese')
elif BMI > 35 :
    print('Extremly Obese')