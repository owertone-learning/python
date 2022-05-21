with open('text_6.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()

local_dict = {}
lessons = {}

for line in content:
    some_str = line.split()
    num = ''
    numbers = []  # объявляю в цикле, чтобы он для каждой новой строки был пустым
    for char in line:
        if char.isdigit():
            num = num + char
        else:
            if num != '':
                numbers.append(int(num))
                num = ''
    if num != '':
        numbers.append(num)
    total = sum(numbers)
    local_dict[some_str[0][:-1]] = total
lessons = {**local_dict}
print(lessons)
