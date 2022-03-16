from random import randint
Random_List_Number= []
len_array = int(input('Plz Enter size of array :  \n'))
while len(Random_List_Number) < len_array :
    Randon_number = randint (0,len_array)
    if Randon_number not in Random_List_Number :
        Random_List_Number.append(Randon_number)


print('Your Array is :\n\t ', Random_List_Number)





#print(t_array)
joon = ['💚','💚','💚','💚','💚']
user_true_char = []


#print(choose_word)


    while True:
        for i in range(len(word)):
            if word[i] in user_true_char :
                print(word[i] , end='')
            else :
                print('-' , end='')
        print(joon)
        user_char = input('Plz enter a char :  ')
        if user_char in word:
            print('Yes')
        else:
            len(joon) -=1
            print ('No')


        if joon == []:
            print('Game over')
            break
