# Работаем с файлом task_2.txt

w = [] # список с кол-вом слов в каждой строке
try:
    with open('task_2.txt', 'r', encoding='utf-8') as f_obj:
        for line in f_obj:
            s1 = line.strip().split()
            w.append(len(s1))
            #print(line.strip().split())
    print(f'Количество строк = {len(w)}\n'
          f'Колво слов построчно: {w}')
except IOError:
    print('Ошибка!')
