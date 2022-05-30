my_list = []  # создаем пустой список

# заполняем его данными
for i in range(5):
    i = input('Введите число: ')
    my_list.append(i)
print(my_list)

# пробегаем по индексам с шагом 2 и меняем его с соседним
# len(my_list) - 1 - потому что нет индекса 5, последний [4]. Индексы с нуля, длина с единицы
for i in range(0, len(my_list) - 1, 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)
