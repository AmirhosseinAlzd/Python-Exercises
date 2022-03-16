num = int(input('Enter your number : '))
num1 = num
Armstrong = 0
Array_number = []
if num == 0 :
    print('yes')
else :
    while (num):
        Array_number.append(num % 10)
        num = int(num / 10)

    for i in range(len(Array_number)):
        Armstrong += Array_number[i] ** len(Array_number)

    check = 'Yes' if (Armstrong == num1 ) else 'No'
    print(check)