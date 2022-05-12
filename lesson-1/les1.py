# получаем от пользователей данные, сохраняем их в переменные и выводим разное всякое
first_name = input('Введите свое имя: ')
age = int(input('Введите свой возраст:'))
weight = int(input('Введите свой вес:'))

print(first_name)
print(type(first_name))
print(age)
print(type(age))
print(f'Ваше имя {first_name}, ваш возраст {age}, ваш вес {weight}. И это все будет строкой')
print(type(f'Ваше имя {first_name}, ваш возраст {age}, ваш вес {weight}'))
print(f'Если мы зачем-то сложим возраст и вес, то получим {age + weight}.  Это будет числом')
print(type(age + weight))
print(f'А если разделим возраст на вес, то получим {age / weight}. И это уже другой тип данных, здесь плавает точка')
print(type(age / weight))

# просто создаем тип данных булево
some_data = True
print(f'Все написанное выше - {some_data}')
print(type(some_data))
