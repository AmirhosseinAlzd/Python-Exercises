def fibonacci(num):
    fibonacci_list = [0, 1]
    if num == 0:
        print('[]')
    elif num == 1:
        print(fibonacci_list[0])
    else:
        for i in range(2, num):
            fibonacci_list.append(fibonacci_list[i - 1] + fibonacci_list[i - 2])
        print(fibonacci_list)


numbers = int(input('\nEnter the number of Fibo : \t\n==> '))
while numbers < 0:
        numbers = int(input('Dont Enter Negetive Number \n\tEnter the number of Fibo'))
fibonacci(numbers)