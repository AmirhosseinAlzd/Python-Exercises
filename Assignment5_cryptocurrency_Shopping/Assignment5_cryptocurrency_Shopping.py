
from os import system
from termcolor import colored


def read_from_file():
    print('is Loading Data from file ...\n\t')
    f = open('Shopping_Data_base.csv' , 'r')

    #my_data = f.read()
    for char in f :
        info = char[:-1].split(',')
        new_dict = {'code' : info[0] , 'name' : info[1] , 'price' : float(info[2]) , 'Inventory' : int(info[3]) , 'Sold' : 0}
        PRODUCTS.append(new_dict)



def add():
    code = input('Enter the code of prouduct : ')
    name = input('Enter the name of prouduct : ')
    price = float(input('Enter the price of prouduct : '))
    Inventory = int(input('Enter the Inventory : '))
    new_dict = {'code' : code , 'name' : name , 'price' : price , 'Inventory' : Inventory , 'sold' : 0 }
    PRODUCTS.append(new_dict)



def edite():
    Show_list()
    choose_number = input('\n\nFor edite , Enter the code of prouduct from above :  ')
    for i in range(len(PRODUCTS)):
        if choose_number == PRODUCTS[i]['code'] :
            PRODUCTS[i]['code'] = input('enter new code :  ')
            PRODUCTS[i]['name'] = input('enter new name :  ')
            PRODUCTS[i]['price'] = float(input('enter new price :  '))
            PRODUCTS[i]['Inventory'] = float(input('enter new Inventory :  '))
            break
        elif i == len(PRODUCTS)-1 :
            print('incorrect code ... \n\n\n\n')
            break



def delete():
    Show_list()
    choose_number = input('\n\nFor Delete , enter the code of prouduct from above : ')
    for i in range(len(PRODUCTS)):
        if choose_number == PRODUCTS[i]['code'] :
            PRODUCTS.pop(i)
            print("\nSuccessfully Deleted")
            break
        elif i == len(PRODUCTS)-1 :
            print('incorrect code ... \n\n\n\n')
            break


def Show_list():
    print('code\t\tname\t\tprice\t\tInventory')
    print('══════════════════════════════════════════════════════════════════')
    for prouduct in PRODUCTS :
        print(prouduct['code'],end = '\t\t')
        print(prouduct['name'],end = '\t\t')
        print(prouduct['price'],end = '\t\t')
        print(prouduct['Inventory'],end = '\t\t')
        print('\n')

def show_Shopping_cart():
    print('code\t\tname\t\tprice\t\tbuy')
    print('══════════════════════════════════════════════════════════════════')
    for prouduct in Shopping_cart :
        print(prouduct['code'],end ='\t\t')
        print(prouduct['name'],end ='\t\t')
        print(prouduct['price'],end ='\t\t')
        print(prouduct['Sold'],end ='\t\t')
        print('\n')

def show_Shopping_cart_in_csv():
    f = open('Shopping_Data_base1.csv' , 'w') 
    f.write('code,name,price,buy\n')

    for prouduct in Shopping_cart :
        f.write(prouduct['code'])
        f.write(',')
        f.write(prouduct['name'])
        f.write(',')
        f.write(str(prouduct['price']))
        f.write(',')
        f.write(str(prouduct['Sold']))
        f.write('\n')


def Search():
    name_product = input('please enter the name of our pruduct : ')
    for i in range(len(PRODUCTS)):
        if name_product == PRODUCTS[i]['name'] :
            print('yes , we have it \n\n')
            Show_list()
            break
        elif i == len(PRODUCTS) -1 :
            print('sorry , we dont have it\n\n')
            Show_list()
            break


def buy():
    array = []
    number = 0
    j = 0
    while True :
        number +=1
        system('clear')
        print('\ninvetory of shopping :\n\n')
        Show_list()
        print('\nmy basket :\n\n')
        show_Shopping_cart()
        print ('\n\n\tchoose your product', number, '( Enter the code of product )' , '   ==>if you want finish your buying  please type "*" \n\n') 
        code_of_product = input()
        if code_of_product != '*':
            for i in range(len(PRODUCTS)) :
                if code_of_product == PRODUCTS[i]['code'] and PRODUCTS[i]['Inventory'] > 0 :
                    numbers_of_product = float(input('\nhow many ??  '))
                    if numbers_of_product <= PRODUCTS[i]['Inventory'] :  
                        print('\n\n\t==>Successfully selected')
                        p = input()
                        PRODUCTS[i]['Inventory'] -= numbers_of_product
                        if code_of_product not in array :
                            array.append(code_of_product)
                            PRODUCTS[i]['Sold'] = numbers_of_product
                            Shopping_cart.append(PRODUCTS[i])
                            break
                        else : 
                            for j in range(len(Shopping_cart)) :
                                if code_of_product == Shopping_cart[j]['code'] :
                                    Shopping_cart[j]['Sold'] += numbers_of_product
                                    break
                            break
                    else :
                        print('\n\n\t ==> Sorry , Product inventory is not enough')
                        p = input()
                        break
                elif code_of_product == PRODUCTS[i]['code'] and PRODUCTS[i]['Inventory'] == 0 :
                    print('\n\n\t ==> Sorry , Product inventory is not enough')
                    p = input()
                    break
                elif code_of_product != PRODUCTS[i]['code'] and  i == len(PRODUCTS) - 1 :
                    print('\n\n\t ==> Sorry , we dont have this Product \n')
                    p = input()
                    break
        elif code_of_product == '*':
            break

def Save_Exit():
    Sum = 0
    show_Shopping_cart()
    show_Shopping_cart_in_csv()
    for i in range(len(Shopping_cart)) :
        Sum += Shopping_cart[i]['price']*Shopping_cart[i]['Sold']
    print('\n\n\n')
    print('╒═════════════════╕')
    print('│ Sum =  ' , Sum ,'  ')
    print('╘═════════════════╛\n')

    f = open('Shopping_Data_base1.csv' , 'a') 
    f.write('Sum : \t')
    f.write(str(Sum))







def show_menu():
    system('clear')
    print('Welcom to our Shopping\n\t')
    print('╒══════════════════════════════════════════════╕')
    print('│              ⟹  ➊ - Add                      │')
    print('│              ⟹  ➋ - Edite                    │')
    print('│              ⟹  ➌ - Delete                   │')
    print('│              ⟹  ➍ - Show list                │')
    print('│              ⟹  ➎ - Search                   │')
    print('│              ⟹  ➏ - Buy                      │')
    print('│              ⟹  ➐ - Save & Exit              │')
    print('╘══════════════════════════════════════════════╛\n')


PRODUCTS = []
Shopping_cart = []
read_from_file()
while True :
    show_menu()
    choose_char = input('Plz choose one of them :  ')
    match choose_char :
        case '1' :
            system('clear')
            add()
            p = input()
        case '2':
            system('clear')
            edite()
            p = input()
        case '3':
            system('clear')
            delete()
            p = input()
        case '4':
            system('clear')
            Show_list()
            p = input()
        case '5':
            system('clear')
            Search()
            p = input()
        case '6':
            system('clear')
            buy()
            p = input()
        case '7':
            system('clear')
            Save_Exit()
            p = input()
            

