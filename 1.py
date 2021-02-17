# Создаем файл task_1.txt

# Запись построчно:
try:
    with open('task_1.txt', 'w', encoding='utf-8') as f_obj:
        s = '1'
        i = 0
        while len(s) > 0:
            if i > 0:
                print(s, file=f_obj)
            s = input('Введите данные: ')
            i += 1
except IOError:
    print('Ошибка!')

# Чтение того, что записали:
try:
    with open('task_1.txt', 'r', encoding='utf-8') as f_obj:
        for line in f_obj:
            print(line.strip())
except IOError:
    print('Ошибка!')
