# Работаем с файлом task_4.txt
# Создаем файл task_4_new.txt

my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

import os
if os.path.exists('task_4_new.txt'):
    os.remove('task_4_new.txt')

try:
    with open('task_4.txt', 'r', encoding='utf-8') as f_obj:
        for line in f_obj:
            s1 = line.strip().split()
            s2 = []
            for x in s1:
                if my_dict.get(x) != None:
                    s2.append(my_dict.get(x))
                else:
                    s2.append(x)
            #print(s2)
            with open('task_4_new.txt', 'a', encoding='utf-8') as f_obj_new:
                print(' '.join(s2), file=f_obj_new)
except IOError:
    print('Ошибка!')
