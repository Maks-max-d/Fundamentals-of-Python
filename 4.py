def degree_func(p: float, q: int):
    """
    This func for degree of
    :param :p is float > 0
    :param :q is int < 0
    :return x1 (с помощью **), x2 (с помощью for):
    """
    try:
        if p <= 0 or q >= 0 or q != int(q):
            x1 = 'Некорректные данные!'
            x2 = 'Некорректные данные!'
        else:
            x1 = p ** q
            x2 = p
            for i in range(-q)[1:]:
                x2 = x2 * p
            x2 = 1 / x2
    except TypeError:
        x1 = 'Некорректные данные!'
        x2 = 'Некорректные данные!'
    except ValueError:
        x1 = 'Некорректные данные!'
        x2 = 'Некорректные данные!'
    return(x1, x2)

p = 2
q = -3

x1, x2 = degree_func(p, q)
print(f'{x1 = }', f'{x2 = }')
