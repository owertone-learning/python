with open('task1.txt') as f:
    content = f.readlines()
    number = 0
    if content[-1] == '\n':
        content = content[:-1]
    print(f'Число строк: {len(content)}')
    for line in content:
        number += 1
        print(f'Число слов в стороке {number}: {len(line.split())}')
