from os import system
from termcolor import colored


WORDS = []
Engilsh_Array = []

def load_data():
    try:
        with open ('/home/amirhossein/Documents/Assigment/Assignment6/translate.txt' , 'r') as d :
            Big_text = d.read()
            lines = Big_text.split('\n')
            for i in range(0 ,len(lines) , 2) :
                my_dict = {'English' : lines[i] , 'Persian' : lines[i+1]}
                WORDS.append(my_dict)
                Engilsh_Array.append(lines[i])
    except FileNotFoundError:
        print('File Not Found')
        exit(0)
    print('Loaded ...')
    #for w in WORDS:
        #print(w)

def Add_New_Word():
    try :
        f = open('/home/amirhossein/Documents/Assigment/Assignment6/translate.txt' , 'a')
    except FileNotFoundError:
        print('File Not Found')
        exit()
    while True :
        char = input('\nPlz Click "Enter" or For exit Enter "*" ')
        if char == '*' :
            break
        else :
            system('clear')
            Eng_Word = (input('Enter your English Word : ')).lower()
            print('\n')
            if Eng_Word in Engilsh_Array or (not (Eng_Word and not Eng_Word.isspace())):
                print(colored('\nThis word is available or Your input is empty. Please add another word' , 'red'))
            else :
                Pers_Word = input('Enter the meaning of word : ').lower()
                f.write('\n'+Eng_Word+'\n'+Pers_Word)
                print(colored('\n\n\t==>Successfully added' , 'green'))
    f.close()

def English2persian():
    user_text = (input('plz write your english text ...')).lower
    user_words = user_text.split(' ')
    output_text = ''
    for user_word in user_words:
        for WORD in WORDS :
            if user_word == WORD['English'] :
                output_text += WORD['Persian'] + ' '
                break
        else :
            output_text += user_word + ' '    
    print(output_text)

    #for user_word in user_words:
    #    for j in range(len(WORDS)) :
    #        if user_word == WORDS[j]['English'] :
    #            output_text += WORDS[j]['Persian'] + ' '
    #            break
    #        elif j == len(WORDS)-1:
    #            output_text += user_word + ' '
    #            break

def persian2English():
    user_text = (input('plz write your persian text ...')).lower()
    user_words = user_text.split(' ')
    output_text = ''
    for user_word in user_words:
        for WORD in WORDS :
            if user_word == WORD['Persian'] :
                output_text += WORD['English'] + ' '
                break
        else :
            output_text += user_word + ' '    
    print(output_text)

def show_menu ():
    system('clear')
    print('Welcom to our Translate :\n\t')
    while True :
        system('clear')
        print('╒══════════════════════════════════════════════╕')
        print('│              ⟹  ➊ - Add New Word             │')
        print('│              ⟹  ➋ - English to Persian       │')
        print('│              ⟹  ➌ - persian to english       │')
        print('│              ⟹  ➍ - Exit                     │')
        print('╘══════════════════════════════════════════════╛\n')
        choose_char = input('Plz choose one of them :  ')
        match choose_char :
            case '1' :
                system('clear')
                Add_New_Word()
            case '2':
                system('clear')
                English2persian()
                p = input()
            case '3':
                system('clear')
                persian2English()
                p = input()
            case '4':
                system('clear')
                exit(0)

load_data()
show_menu ()
