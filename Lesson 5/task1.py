input_data = open('task1.txt', 'w', encoding='utf-8')

while True:
    local_data = input('Введите данные: ')
    print(local_data)
    input_data.writelines(f'{local_data}\n')
    if len(local_data) == 0:
        break
input_data.close()
