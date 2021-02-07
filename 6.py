def int_func(s: str):
    """
    This func for capitalizing a word
    :param :s is str
    :return cap_s:
    """
    try:
        cap_s = str(s).capitalize()
    except TypeError:
        cap_s = ''
    except ValueError:
        cap_s = ''
    return(cap_s)

print(int_func('text'), int_func(12344))


# 2-я часть задания
s = 'hellow world    hellow python 123 ABC'
int_func_1 = lambda s: ' '.join([int_func(str(s.split()[i])) for i in range(len(s.split()))])
print(int_func_1(s))
