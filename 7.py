# Работаем с файлом task_7.txt
# Создаем файл task_7_j.json

import json

firm_profit = {}
avg_profit = [0, 0]

try:
    with open('task_7.txt', 'r', encoding='utf-8') as f_obj:
        for line in f_obj:
            s = line.strip().split()
            try:
                firm_profit.update({s[0]: float(s[2]) - float(s[3])})
                if float(s[2]) - float(s[3]) >= 0:
                    avg_profit[0] += float(s[2]) - float(s[3])
                    avg_profit[1] += 1
            except TypeError:
                firm_profit.update({s[0]: '---'})
            except ValueError:
                firm_profit.update({s[0]: '---'})
        if avg_profit[1] > 0:
            my_list = [firm_profit, {'average_profit': avg_profit[0]/avg_profit[1]}]
        else:
            my_list = [firm_profit]
        print(my_list)
        with open('task_7_j.json', 'w') as f_json:
            json.dump(my_list, f_json)
except IOError:
    print('Ошибка!')

try:
    with open('task_7_j.json') as f_json:
        data_loaded = json.load(f_json)
        print(data_loaded)
except IOError:
    print('Ошибка!')
