num1 , num2 = int(input('Enter your first number : ')) , int(input('Enter your second number : ')) 
LCM =0
while num1 <= 0 or num2 <= 0 :
    num1 , num2 = int(input('Error! Enter positive number for your first number')) , int(input('Error! Enter positive number for your second number'))

max_num = max(num1, num2)
for i in range(max_num, num1 * num2 + 1):
    if (i % num1 == 0) and (i % num2 == 0):
        LCM = i
        break
print('Least common multiple : ', LCM)