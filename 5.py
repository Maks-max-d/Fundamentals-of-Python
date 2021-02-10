from functools import reduce

def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el

my_list = [x for x in range(100, 1000 + 1) if x % 2 == 0]

print(my_list)
print(reduce(my_func, my_list))
