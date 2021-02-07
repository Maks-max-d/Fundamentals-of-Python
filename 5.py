def list_sum():
    """
    This func for sum of all int/float input elements
    """
    el_sum = 0
    k = 0
    s = 'a'
    end_of_func = 0
    while len(s) > 0:
        if k > 0:
            s_list = s.split()
            for i in range(len(s_list)):
                try:
                    el_sum += float(s_list[i])
                except TypeError:
                    end_of_func = 1
                except ValueError:
                    end_of_func = 1
        k += 1
        print(el_sum)
        if end_of_func == 1:
            break
        s = input('Введите числа через пробел (нечисловой символ = конец расчета): ')

list_sum()