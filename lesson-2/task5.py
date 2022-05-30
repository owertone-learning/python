my_list = [9, 7, 5, 3, 3, 3, 3, 2]
print(my_list)
new_number = int(input('Enter some number: '))

# если такая цифра есть, то нужно ее разместить в правильном месте
if my_list.count(new_number) > 0:
    # рассчитываем индекс размещения в зависимости от количества вхождений (индекс первого вхождения + кол-во вхождений)
    place = my_list.index(new_number) + my_list.count(new_number)
    # размещаем цифру в рассчитанный выше индекс
    my_list.insert(place, new_number)
    print(my_list)

# если такой цифры нет, нужно найти ей правильное место (в начале/конце)

else:
    print('Ищем место...')
    i = 0
    while i != len(my_list):
        number = my_list[i]
        if new_number > number:
            my_list.insert(my_list.index(number), new_number)
            break
        else:
            i += 1
    else:
        my_list.append(new_number)
    print(my_list)


