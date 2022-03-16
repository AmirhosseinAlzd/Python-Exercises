from os import system
import os
from random import randint
import random
from time import time
from termcolor import colored


def calculate_time(start_time):
    return time() - start_time


def Show_game_board():
    for i in range(3):
        print('\t\t\t\t\t\t\t\t\t' , end='')
        for j in range(3):
            print(game[i][j] , end='\t')
        print('\n')


def player_1_game() :
    Player_1 = input('Player 1 :\n\tPlz choose unselected place : ( Enter number :  ')
    while (Player_1 in choose_place) or (Player_1 not in game_place):
        Player_1 = input('Player 1 :\n\tPlz choose unselected place and True Number : ( Enter number :  ')
    choose_place.append(Player_1)
    match Player_1 :
        case '1' :
            game[0][0] = colored('X' , 'red')
        case '2' :
            game[0][1] = colored('X' , 'red')
        case '3' :
            game[0][2] = colored('X' , 'red')
        case '4' :
            game[1][0] = colored('X' , 'red')
        case '5' :
            game[1][1] = colored('X' , 'red')
        case '6' :
            game[1][2] = colored('X' , 'red')
        case '7' :
            game[2][0] = colored('X' , 'red')
        case '8' :
            game[2][1] = colored('X' , 'red')
        case '9' :
            game[2][2] = colored('X' , 'red')



def player_2_game():
    Player_2 = input('Player 2 :\n\tPlz choose unselected place : ( Enter number :  ')
    while Player_2 in choose_place or Player_2 not in game_place:
        Player_2 = input('Player 2 :\n\tPlz choose unselected place and True Number: ( Enter number :  ')
    choose_place.append(Player_2)
    match Player_2 :
        case '1' :
            game[0][0] = colored('O' , 'blue')
        case '2' :
            game[0][1] = colored('O' , 'blue')
        case '3' :
            game[0][2] = colored('O' , 'blue')
        case '4' :
            game[1][0] = colored('O' , 'blue')
        case '5' :
            game[1][1] = colored('O' , 'blue')
        case '6' :
            game[1][2] = colored('O' , 'blue')
        case '7' :
            game[2][0] = colored('O' , 'blue')
        case '8' :
            game[2][1] = colored('O' , 'blue')
        case '9' :
            game[2][2] = colored('O' , 'blue')

def player_computer_game() :
    computer = random.choice(game_place)
    while computer in choose_place :
        computer = random.choice(game_place)
    choose_place.append(computer)
    match computer :
        case '1' :
            game[0][0] = colored('O' , 'blue')
        case '2' :
            game[0][1] = colored('O' , 'blue')
        case '3' :
            game[0][2] = colored('O' , 'blue')
        case '4' :
            game[1][0] = colored('O' , 'blue')
        case '5' :
            game[1][1] = colored('O' , 'blue')
        case '6' :
            game[1][2] = colored('O' , 'blue')
        case '7' :
            game[2][0] = colored('O' , 'blue')
        case '8' :
            game[2][1] = colored('O' , 'blue')
        case '9' :
            game[2][2] = colored('O' , 'blue')



### player & player
def play_Vs_play():
    win = False
    Player_1 = '0'
    Player_2 = '0'
    while True :
        os.system("clear")
        Show_game_board()
        player_1_game()
        for w in range(3):
            if game[w][0] == game[w][1] == game[w][2] == colored('X' , 'red') :
                os.system("clear")
                Show_game_board()
                print('player 1 win the game')
                win = True
                break
        for w in range(3):
            if game[0][w] == game[1][w] == game[2][w] == colored('X' , 'red') :
                os.system("clear")
                Show_game_board()
                print('player 1 win the game')
                win = True
                break
        if game[0][0] == game[1][1] == game[2][2] == colored('X' , 'red')  or  game[0][2] == game[1][1] == game[2][0] == colored('X' , 'red') :
            os.system("clear")
            Show_game_board()
            print('player 1 win the game')
            win = True
            break
        if win == True :
            pause1 = input()
            break

    ###Equal :

        if len(choose_place) == 9 :
            os.system("clear")
            Show_game_board()
            print('Equal')
            pause = input()
            break

    ###player_2

        Show_game_board()
        player_2_game()
        os.system("clear")

        Show_game_board()
        for w in range(3):
            if game[w][0] == game[w][1] == game[w][2] == colored('O' , 'blue') :
                print('player 2 win the game')
                win = True
                break
        for w in range(3):
            if game[0][w] == game[1][w] == game[2][w] == colored('O' , 'blue') :
                print('player 2 win the game')
                win = True
                break
        if game[0][0] == game[1][1] == game[2][2] == colored('O' , 'blue')  or  game[0][2] == game[1][1] == game[2][0] == colored('O' , 'blue') :
            print('player 2 win the game')
            win = True
            break
        if win == True :
            pause2 = input()
            break
        
        
        ##################################################################################################
def play_with_computer():
    win = False
    Player_1 = '0'
    Computer = '0'
    while True :
        os.system("clear")
        Show_game_board()
        player_1_game()
        for w in range(3):
            if game[w][0] == game[w][1] == game[w][2] == colored('X' , 'red') :
                os.system("clear")
                Show_game_board()
                print('You win the game')
                win = True
                break
        for w in range(3):
            if game[0][w] == game[1][w] == game[2][w] == colored('X' , 'red') :
                os.system("clear")
                Show_game_board()
                print('You win the game')
                win = True
                break
        if game[0][0] == game[1][1] == game[2][2] == colored('X' , 'red')  or  game[0][2] == game[1][1] == game[2][0] == colored('X' , 'red') :
            os.system("clear")
            Show_game_board()
            print('You win the game')
            win = True
            break
        if win == True :
            pause1 = input()
            break

    ###Equal :

        if len(choose_place) == 9 :
            os.system("clear")
            Show_game_board()
            print('Equal')
            pause = input()
            break

    ###computer

        Show_game_board()
        player_computer_game()
        os.system("clear")

        Show_game_board()
        for w in range(3):
            if game[w][0] == game[w][1] == game[w][2] == colored('O' , 'blue') :
                print('You lost')
                win = True
                break
        for w in range(3):
            if game[0][w] == game[1][w] == game[2][w] == colored('O' , 'blue') :
                print('You lost')
                win = True
                break
        if game[0][0] == game[1][1] == game[2][2] == colored('O' , 'blue') or  game[0][2] == game[1][1] == game[2][0] == colored('O' , 'blue') :
            print('You lost')
            win = True
            break
        if win == True :
            pause2 = input()
            break
    

game =[['➊','➋','➌'],
       ['➍','➎','❻'],
       ['➐','➑','➒']]

choose_place = []
game_place = ['1','2','3','4','5','6','7','8','9']



Megamenu = input('1 - Single Player\n2 - Multi Player\n3 - Exit\n\n\t select one of them : ')
match Megamenu :
    case '1' : 
        start_time = time()
        play_Vs_play()
        print('\n\n\tMatch Duration (Single Player): ', calculate_time(start_time))
    case '2' :
        start_time = time()
        play_with_computer()
        print('\n\n\tMatch Duration ( Multi Player ): ', calculate_time(start_time))
    case '3' :
        system('clear')
        print('Thank You !')
        exit(0)
