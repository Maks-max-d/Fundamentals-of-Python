s = input('Введите строку: ')
my_list = s.split()

for ind, el in enumerate(my_list):
    #print(my_list[el])
    if ind > 0:
        my_str = my_str + '\n'
    else:
        my_str = ''
    my_str = my_str + str(ind + 1) + '. ' + el[0:10]

print(my_str)
#fffffffffaaaaaa 87 12345678910 12 rrrr s zdbfdbzd
