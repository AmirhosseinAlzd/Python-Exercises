import os
from random import randint
from os import system
import random


word_bank_clothes = ['cardigan' , 'coat' , 'jacket' , 'jeans' , 'top' , 'pants' , 'sweater' , 'skirt' , 'warm up suit' , 'hat']
word_bank_animals = ['bee' , 'fly' , 'mosquito' , 'spider' , 'chicken' , 'bird' , 'bear' , 'camel', 'sheep' , 'jellyfish']
word_bank_cities = ['mashhad' , 'abadan' , 'ankara' , 'berlin' , 'tehran' , 'doshanbe' , 'london' , 'torento', 'tabriz' , 'sanandaj']
word_bank_computer = ['keyboard' , 'computer' , 'ram' , 'rom' , 'gate' , 'ssd' , 'hdd' , 'nvme', 'monitor' , 'battery']
word_bank_football = ['chelsea' , 'arsenal' , 'manchester' , 'psg' , 'bayern' , 'davarcelona' , 'juv' , 'zenit', 'padide' , 'everton']
word_bank_sport = ['baseball' , 'basketball' , 'boxin' , 'cycling' , 'golf' , 'volleyball' , 'tennis' , 'soccer', 'skiing' , 'rugby']
word_bank_actor = ['tom hanks' , 'keanu reeves' , 'leonardo dicaprio' , 'will smith' , 'dwayne johnson' , 'tom cruise' , 'sxarlett johansson' , 'mark ruffalo', 'ben affleck' , 'margot robbie']
word_bank_fruits = ['apple' , 'banana' , 'kiwi' , 'peach' , 'guava' , 'orange' , 'berry' , 'cherry', 'litchi' , 'melon']


array_choose = []
t_array = []
counter_win = 1
joon = ['💚','💚','💚','💚','💚']


while True :
    os.system("clear")
    print('╒══════════════════════════════════════════════╕')
    print('│⟹  ➊ - New Game                               │')
    print('│⟹  ➋ - Exit                                   │')
    print('╘══════════════════════════════════════════════╛\n')
    menu_1 = input('\n\tPlease Choose one of them : ')
    os.system("clear")
    if menu_1 == '1' :
        print('╒══════════════════════════════════════════════╕')
        print('│              ⟹  ➊ - Clothes                  │')
        print('│              ⟹  ➋ - Animals                  │')
        print('│              ⟹  ➌ - Cities                   │')
        print('│              ⟹  ➍ - Computer                 │')
        print('│              ⟹  ➎ - Football                 │')
        print('│              ⟹  ➏ - Sport                    │')
        print('│              ⟹  ➐ - Actors                   │')
        print('│              ⟹  ➑ - Ftuits                   │')
        print('╘══════════════════════════════════════════════╛\n')
        Contents_choice = input('plz choose one of the subjects(Enter number...) : \n\t ==> ')
        match Contents_choice :
            case '1' : 
                t_array = word_bank_clothes
            case '2' :
                t_array = word_bank_animals
            case '3' :
                t_array = word_bank_cities
            case '4' :
                t_array = word_bank_computer
            case '5' :
                t_array = word_bank_football
            case '6' :
                t_array = word_bank_sport
            case '7' :
                t_array = word_bank_actor
            case '8' :
                t_array = word_bank_fruits

        user_true_char = []
        counter_win = 0
        joon = ['💚','💚','💚','💚','💚']
        word = random.choice(t_array)
        if word in array_choose :
            while word in array_choose :
                word = random.choice(t_array)
        array_choose.append(word)
        while True:
            os.system("clear")
            print('\n╒════════════════════════════╕')
            print('│',end='')
            for i in range (len(joon)) :
                print('  ' ,joon[i],end='')
            print('   │                           ',end='')
            
            for i in range(len(word)):
                #print(' ')
                if word[i] in user_true_char :
                    print(word[i] , end='')
                elif word[i]==' ' :
                    print(' ' , end='')
                else:
                    print('-' , end='')
            
            print('\n╘════════════════════════════╛\n')
            if joon != [] and counter_win < len(word) :
                user_char = input('\nPlz enter a char :  ')
                if user_char in word:
                    print('Yes')
                    user_true_char.append(user_char)
                    counter_win +=1
                else:
                    joon.pop()
                    print ('No')

            if joon == []:
                os.system("clear")
                print('\n╒════════════════════════════╕')
                print('│        Game Over 😱        │')
                print('╘════════════════════════════╛\n')
                pause = input()
                array_choose = []
                break

            if counter_win >= len(word) :
                os.system("clear")
                print('\n╒════════════════════════════╕')
                print('│        You win  👏👏👏     │')
                print('╘════════════════════════════╛\n')
                pause = input()
                break
    elif menu_1 == '2':
        exit(0)
