my_list = ['abc', '!+_-', 5, 87.589, True, 237, ['dfr', 123, False], {1, 2}]
print(my_list)

my_list_1 = my_list[::2]
my_list_2 = my_list[1::2]

for el in range(len(my_list)):
    if el % 2 > 0:
        change_el = my_list.pop(el)
        my_list.insert(el - 1, change_el)

print(my_list)
