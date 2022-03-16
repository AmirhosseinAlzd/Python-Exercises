len_Array=int(input(('Lets make a Array list together\n1- first Enter the size of your Array :\n\t==> ')))
Array = []
print('2- Now Enter your number : \n')
for i in range(0,len_Array) :
    print('Number ' , i+1 , ' : ' , end='')
    value = int(input())
    Array.append(value)

print(Array)

i = 0
j = 1
c = 1
while j<len_Array :
    if Array[i]<Array[j] :
        c +=1
    i +=1
    j +=1

check = 'Yes' if (c == len_Array) else 'NO'
print(check)
