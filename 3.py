# Работаем с файлом task_3.txt

def avg(s):
    """
    This func for avg of all float list elements
    :param :s is list
    :return s_avg
    """
    try:
        s_avg = sum(s) / len(s)
    except TypeError:
        s_avg = 'Некорректные данные!'
    except ValueError:
        s_avg = 'Некорректные данные!'
    return(s_avg)

employee_name = []
employee_salary = []

try:
    with open('task_3.txt', 'r', encoding='utf-8') as f_obj:
        i = 0
        for line in f_obj:
            i += 1
            s1 = line.strip().split()
            employee_name.append(s1[0])
            employee_salary.append(float(s1[1]))
    employee_1 = [employee_name[i] for i in [ind for ind, el in enumerate(employee_salary) if float(el) < 20000]]
    salary_avg_1 = avg([el for ind, el in enumerate(employee_salary) if float(el) < 20000])
    salary_avg_all = avg(employee_salary)
    print(f'Сотрудники с окладом < 20 тыс. руб.: {employee_1}')
    print(f'Сотрудники с окладом < 20 тыс. руб., средний оклад: {salary_avg_1}')
    print(f'Все сотрудники, средний оклад: {salary_avg_all}')
except IOError:
    print('Ошибка!')
