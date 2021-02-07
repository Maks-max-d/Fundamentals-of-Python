def my_func(x1: float, x2: float, x3: float):
    """
    This func for sum of two max elements
    :param :x1 is float
    :param :x2 is float
    :param :x3 is float
    :return x:
    """
    my_list = [x1, x2, x3]
    try:
        my_list.sort()
        x = my_list[1] + my_list[2]
    except TypeError:
        x = 'Некорректные значения!'
    except ValueError:
        x = 'Некорректные значения!'
    return x

x1 = 9.5
x2 = 8.3
x3 = 15.7

x = my_func(x1, x2, x3)
print(f'{x = }')
