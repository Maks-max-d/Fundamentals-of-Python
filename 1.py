def division():
    """
    This func for division
    :d1 dividend:
    :d2 divisor:
    :return d1/d2:
    """
    d1 = input('Введите делимое: ')
    d2 = input('Введите делитель: ')
    #d = d1 / d2 if d2 != 0 else 'Деление на 0!'
    try:
        d = float(d1) / float(d2)
    except ZeroDivisionError:
        d = 'Деление на 0!'
    except ValueError:
        d = 'Некорректные значения!'
    return d

d = division()
print(d)
