# Создаем файл task_5.txt

# Запись чисел в файл:
try:
    with open('task_5.txt', 'w', encoding='utf-8') as f_obj:
        s = input('Введите числа через пробел: ')
        print(s, file=f_obj)
except IOError:
    print('Ошибка!')

# Чтение и подсчет суммы:
try:
    with open('task_5.txt', 'r', encoding='utf-8') as f_obj:
        for line in f_obj:
            s = line.strip().split()
            try:
                s_sum = sum([float(x) for x in s])
            except TypeError:
                s_sum = '---'
            except ValueError:
                s_sum = '---'
        print(f'Сумма чисел в файле: {s_sum}')
except IOError:
    print('Ошибка!')
