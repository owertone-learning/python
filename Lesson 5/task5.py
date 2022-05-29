with open('text_5.txt', 'w', encoding='utf-8') as f:
    numbers = (num for num in range(1, 11))
    num_list = ','.join(map(str, numbers))
    f.writelines(f'{num_list}')

with open('text_5.txt', 'r', encoding='utf-8') as f:
    content = f.readline()
for n in content:
    num_list = map(int, content.split(','))
print(f'Сумма чисел: {sum(num_list)}')
