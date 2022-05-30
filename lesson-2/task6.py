number = 1
propers = {'Название': 'Macbook', 'Цена': '3000', 'Количество': '5', 'Ед.': 'шт.'}
#catalog = []
sku = (number, propers)
catalog = [sku]


while True:
    ask = input('Хотите добавить товар? Да/Нет: ')
    if 'Да' in ask or 'да' in ask:
        number += 1
        name = input('Введите название: ')
        price = input('Введите цену: ')
        amount = input('Введите количество: ')
        unit = input('Введите единицу измерения: ')
        local_propers = {}
        local_propers['Название'] = name
        local_propers['Цена'] = price
        local_propers['Количество'] = amount
        local_propers['Ед.'] = unit
        sku = (number, {**local_propers})
        catalog.insert(number, sku)
    else:
        break

print(f'Каталог: {catalog}')

"""Создаем аналитику"""


def analitics(data_tpl):
    list_to_tuple = None
    data_analytics = {}
    local_dict = {}
    for i in data_tpl:
        list_to_tuple = i
        first, second = list_to_tuple
        for k, v in second.items():
            if v.isdigit():
                local_dict.setdefault(k, []).append(int(v))
            else:
                local_dict.setdefault(k, []).append(v)
    data_analytics = {**local_dict}
    print('-------------------------')
    print(f'Аналитика: {data_analytics}')



analitics(catalog)
