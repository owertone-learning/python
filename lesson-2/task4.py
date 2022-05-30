my_str = input('Введите несколько слов: ')

my_str = my_str.split()
for i, j in enumerate(my_str, 1):
    print(f'{i}) {j[0:10]}')
