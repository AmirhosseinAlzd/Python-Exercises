num1 , num2 = int(input('Enter your first number : ')) , int(input('Enter your second number : ')) 
GCD =0
while num1 <= 0 or num2 <= 0 :
    num1 , num2 = int(input('Error! Enter positive number for your first number')) , int(input('Error! Enter positive number for your second number'))

mini_num = min(num1 , num2)
for i in range(1,mini_num+1):
    if (num1 % i == 0) and (num2 % i == 0):
        GCD = i

print('Greatest common divisor : ' , GCD)