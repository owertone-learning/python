months = [
    {'name': 'Январь', 'season': 'зима'},
    {'name': 'Февраль', 'season': 'зима'},
    {'name': 'Март', 'season': 'весна'},
    {'name': 'Апрель', 'season': 'весна'},
    {'name': 'Май', 'season': 'весна'},
    {'name': 'Июнь', 'season': 'лето'},
    {'name': 'Июль', 'season': 'лето'},
    {'name': 'Август', 'season': 'лето'},
    {'name': 'Сентярь', 'season': 'осень'},
    {'name': 'Октябрь', 'season': 'осень'},
    {'name': 'Ноябрь', 'season': 'осень'},
    {'name': 'Декабрь', 'season': 'зима'}
]

month_name = None
month = int(input('Введите порядковый номер месяца: '))

if 0 < month <= 12:
    for month_name in months:
        month_name = months[month - 1]
    print(f"Месяц {month_name.get('name')}, время года - {month_name.get('season')}")
    # print(f"Месяц {month_name.setdefault('name')}, время года - {month_name.setdefault('season')}")  // тоже работает

else:
    print('Месяца с таким номером не существует')
