from view import *

def main():
    while True:
        print('Привет вот функционал: \n1 -получить все товары,\n2- получить определенный товар, \n3 - создать товар, \n4 - удалить товар, \n5 - обновить товар') 
        method = input('Введите число: ')
        
        if method == '1':
            print(get_obj())
        
        elif method == '2':
            id = int(input('Введи id товара: '))
            print(get_one_obj(id))
        
        elif method == '3':
            print(post_obj())
        
        elif method == '4':
            id = int(input('Введи id товара который хотите удалить: '))
            print(delete_obj(id))
        
        elif method == '5':
            id = int(input('Введи id товара который хотите обновить: '))
            print(update_obj(id))


if __name__ == '__main__': 
    main()
