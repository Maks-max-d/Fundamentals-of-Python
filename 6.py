# Работаем с файлом task_6.txt

my_dict = {}
try:
    with open('task_6.txt', 'r', encoding='utf-8') as f_obj:
        for line in f_obj:
            s = line.strip().split()
            s_time = 0
            key = s[0].replace(':', '')
            for i in range(1, len(s)):
                if s[i] == '—':
                    s_time += 0
                else:
                    s_time += float(s[i][0:s[i].index('(')])
            my_dict.update({key: s_time})
        print(my_dict)
except IOError:
    print('Ошибка!')
