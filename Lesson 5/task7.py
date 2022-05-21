import json

with open('text_7.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()


def print_data(content):
    firms = {}
    profit_list = []
    ap = {}
    for line in content:
        firm = line.split()
        profit = int(firm[2]) - int(firm[3])
        profit_list.append(profit)
        firms[' '.join([firm[1], firm[0]])] = profit

    local_list = []
    for num in profit_list:
        if num > 0:
            local_list.append(num)
    ap['averadge_profit'] = sum(local_list) / len(local_list)
    data = [firms, ap]

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print('Данные загружены!')


print_data(content)
