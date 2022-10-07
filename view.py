import datetime
import json

# [
#     {
#         "id": 1,
#         "name": "John",
#         "price": 29,
#         "time": "2022-10-07 19:59:47.076531",
#         "description": "jfnls",
#         "status": "sell"
#     }, {
    #     "id": 2,
    #     "name": "Snow",
    #     "price": 100,
    #     "time": "2022-10-07 19:59:47.076531",
    #     "description": "jfnls",
    #     "status": "sales"
    # }
# ]

def get_obj(ge_price = None, le_price = None,data = None, status = None):
    with open('shop.json') as file:
        s = json.load(file)
    if ge_price:
        new_s = [i for i in s if i['price'] >= ge_price]
        return new_s
    if le_price:
        new_s = [i for i in s if i['price'] <= le_price]
        return new_s
    if data:
        new_s =[i for i in s if str(data) in i['time']]
        return new_s
    if status:
        new_s =[i for i in s if i['status'] == status]
        if status == 'sell':
            return new_s
        elif status == 'sales':
            return new_s

    return s


def get_one_obj(id):
    s = get_obj()
    one_obj = [i for i in s if i['id'] == id]
    if one_obj:
        return one_obj[0]

    return 'нет такого товара'
    

def update_obj(id):
    s = get_obj()
    new_s = [ i for i in s if i['id'] == id]
    if new_s:
        new_s[0]['name'] = input('New name: ')
        new_s[0]['price'] = float(input('New price: '))
        new_s[0]['time_update'] = f'{datetime.datetime.today()}'
        new_s[0]['description'] = input('New description: ')
        new_s[0]['status'] = input('New status: ')
        json.dump(s, open('shop.json', 'w'))
        return s
    
    return 'нет такого товара'



def delete_obj(id):
    s = get_obj()
    new_s = [i for i in s if i['id'] == id]
    if new_s:
        s.remove(new_s[0])
    with open('shop.json', 'w') as file:
        json.dump(s, file)
        
    return 'нет такого товара'



def post_obj():
    s = get_obj()
    max_i = max(i['id'] for i in s)
    s.append({
        'id': max_i + 1, 
        'name': input('Name: '),
        'price': float(input('Price: ')), 
        "time": f'{datetime.datetime.today()}', 
        "time_update": None,  
        "description": input('Description: '), 
        "status": input('Status: ')})
    with open('shop.json', 'w') as file:
        json.dump(s, file)
        return s
    



