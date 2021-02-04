my_list = [7, 5, 3, 3, 2]
print(my_list)
el_new = int(input('Введите новый элемент рейтинга: '))

i = -1
if el_new > my_list[0]:
    my_list.insert(0, el_new)
elif el_new <= my_list[len(my_list) - 1]:
    my_list.append(el_new)
else:
    for ind, el in enumerate(my_list):
        if el_new <= el:
            i = ind
    my_list.insert(i + 1, el_new)

print(my_list)